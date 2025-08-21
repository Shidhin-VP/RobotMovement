import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:lottie/lottie.dart';
import 'package:mobilefrontend/homePage.dart';
import 'package:mobilefrontend/textProvider.dart';
import 'package:provider/provider.dart';
import 'package:web_socket_channel/web_socket_channel.dart';

class Connectionpage extends StatefulWidget {
  const Connectionpage({super.key});

  @override
  State<Connectionpage> createState() => _ConnectionpageState();
}

class _ConnectionpageState extends State<Connectionpage> {
  final TextEditingController _moveto = TextEditingController();
  final TextEditingController _moveArm = TextEditingController();
  late WebSocketChannel channel;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      setState(() {
        channel = context.read<TextProvider>().channel!;
      });
    });
  }

  void sendRos(String command) {
    try {
      final message = {
        "op": "publish",
        "topic": "/Phase2Topic",
        "msg": {"data": command},
      };
      final jsonMessage = jsonEncode(message);
      channel.sink.add(jsonMessage);
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          backgroundColor: Colors.greenAccent,
          content: Center(child: Text("Message Sent!")),
          duration: Duration(milliseconds: 1500),
        ),
      );
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          backgroundColor: Colors.orangeAccent,
          content: Center(child: Text("Error $e")),
          duration: Duration(milliseconds: 1500),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          final movearmTrimer = _moveArm.text.isNotEmpty
              ? _moveArm.text.split(RegExp(r'[,\s]+'))
              : [];
          final movetoTrimer = _moveto.text.isNotEmpty
              ? _moveto.text.split(RegExp(r'[,\s]'))
              : [];
          if (movearmTrimer.isNotEmpty && movearmTrimer.last == "") {
            movearmTrimer.removeLast();
          } else if (movetoTrimer.isNotEmpty && movetoTrimer.last == "") {
            movetoTrimer.removeLast();
          }
          if ((_moveArm.text.isNotEmpty ^ _moveto.text.isNotEmpty) &&
              ((_moveArm.text.isNotEmpty && movearmTrimer.length >= 4) ||
                  (_moveto.text.isNotEmpty && movetoTrimer.length >= 3))) {
            setState(() {
              _moveArm.text = _moveArm.text.isNotEmpty
                  ? "${movearmTrimer[0]},${movearmTrimer[1]},${movearmTrimer[2]},${movearmTrimer[3]}"
                  : "";
              _moveto.text = _moveto.text.isNotEmpty
                  ? "${movetoTrimer[0]},${movetoTrimer[1]},${movetoTrimer[2]}"
                  : "";
            });
            final String command = _moveto.text.isNotEmpty
                ? "move to|${movetoTrimer[0]}, ${movetoTrimer[1]}, ${movetoTrimer[2]}"
                : "move arm|${movearmTrimer[0]}, ${movearmTrimer[1]}, ${movearmTrimer[2]}, ${movearmTrimer[3]}";
            sendRos(command);
          } else {
            ScaffoldMessenger.of(context).showSnackBar(
              SnackBar(
                backgroundColor: Colors.orangeAccent,
                duration: Duration(milliseconds: 1500),
                content: Center(
                  child: Text(
                    "Enter Data to One of the Fields, and Give exact required values",
                  ),
                ),
              ),
            );
          }
        },
        child: Icon(Icons.send_outlined),
      ),
      appBar: AppBar(
        actions: [
          IconButton(
            color: Colors.redAccent,
            onPressed: () {
              channel.sink.close();
              context.read<TextProvider>().setChannelChecker(false);
              ScaffoldMessenger.of(context).showSnackBar(
                SnackBar(
                  backgroundColor: Colors.lightBlueAccent,
                  duration: Duration(milliseconds: 1500),
                  content: Center(
                    child: Center(
                      child: Text(
                        "Session Closed",
                        style: TextStyle(color: Colors.brown),
                      ),
                    ),
                  ),
                ),
              );
              Navigator.of(
                context,
              ).pushReplacement(MaterialPageRoute(builder: (_) => Homepage()));
            },
            icon: Icon(Icons.close_rounded, color: Colors.redAccent),
          ),
        ],
        title: Text(
          "Controller",
          style: TextStyle(fontSize: 20, fontFamily: "Federant"),
        ),
        centerTitle: true,
        elevation: 5,
      ),
      body: Stack(
        children: [
          Positioned.fill(
            child: LottieBuilder.asset(
              "assets/lottie/Robotic Claw.json",
              fit: BoxFit.contain,
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(24.0),
            child: Column(
              children: [
                SizedBox(height: 100),
                AnimatedLabelTextField(
                  label: "Move To",
                  hintText: "Enter X, Y, Z",
                  controller: _moveto,
                ),
                SizedBox(height: 30),
                AnimatedLabelTextField(
                  label: "Move Arm",
                  hintText: "Enter X, Y, Z, W",
                  controller: _moveArm,
                ),
                SizedBox(height: 30),
                ElevatedButton(
                  style: ButtonStyle(
                    surfaceTintColor: WidgetStatePropertyAll(Colors.red),
                  ),
                  onPressed: () {
                    sendRos("0");
                  },
                  child: Text(
                    "Emergency Abort",
                    style: TextStyle(color: Colors.redAccent),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class AnimatedLabelTextField extends StatefulWidget {
  final String label;
  final String hintText;
  final TextEditingController controller;

  const AnimatedLabelTextField({
    super.key,
    required this.label,
    required this.hintText,
    required this.controller,
  });

  @override
  State<AnimatedLabelTextField> createState() => _AnimatedLabelTextFieldState();
}

class _AnimatedLabelTextFieldState extends State<AnimatedLabelTextField> {
  final FocusNode _focusNode = FocusNode();
  bool _hasFocus = false;

  @override
  void initState() {
    super.initState();

    _focusNode.addListener(() {
      setState(() {
        _hasFocus = _focusNode.hasFocus;
      });
    });
  }

  @override
  void dispose() {
    _focusNode.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final baseColor = Colors.grey[600]!;
    final focusColor = Colors.deepPurple;

    return Row(
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        AnimatedDefaultTextStyle(
          duration: Duration(milliseconds: 1500),
          style: TextStyle(
            fontSize: _hasFocus ? 20 : 16,
            fontWeight: _hasFocus ? FontWeight.w700 : FontWeight.w500,
            color: _hasFocus ? focusColor : baseColor,
            fontFamily: "Federant",
          ),
          child: Text(widget.label),
        ),
        SizedBox(width: 12),
        Expanded(
          child: TextField(
            inputFormatters: [
              FilteringTextInputFormatter.allow(RegExp(r'[0-9,]')),
            ],
            controller: widget.controller,
            focusNode: _focusNode,
            decoration: InputDecoration(
              hintText: widget.hintText,
              contentPadding: EdgeInsets.symmetric(
                vertical: 14,
                horizontal: 12,
              ),
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(12),
                borderSide: BorderSide(
                  color: _hasFocus ? focusColor : Colors.grey.shade400,
                  width: 2,
                ),
              ),
              focusedBorder: OutlineInputBorder(
                borderRadius: BorderRadius.circular(12),
                borderSide: BorderSide(color: focusColor, width: 2),
              ),
            ),
          ),
        ),
      ],
    );
  }
}
