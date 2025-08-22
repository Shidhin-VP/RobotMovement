import 'package:flutter/material.dart';
import 'package:phase3frontend/connectionPage.dart';
import 'package:phase3frontend/textProvider.dart';
import 'package:provider/provider.dart';
import 'package:web_socket_channel/io.dart';
import 'package:web_socket_channel/web_socket_channel.dart';

class Homepage extends StatefulWidget {
  const Homepage({super.key});

  @override
  State<Homepage> createState() => _HomepageState();
}

class _HomepageState extends State<Homepage> {
  final TextEditingController _controller = TextEditingController();
  bool connect = false;
  String? IP;
  WebSocketChannel? channel;

  Future<(bool, WebSocketChannel)> connectChannel(String ipText) async {
    channel = IOWebSocketChannel.connect("ws://$ipText:9090");
    try {
      await channel!.ready;
      return (true, channel!);
    } catch (e) {
      return (false, channel!);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Home Page", style: TextStyle(fontFamily: "Federant")),
        centerTitle: true,
        elevation: 5,
      ),
      body: SafeArea(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Center(
              child: Stack(
                children: [
                  TextField(
                    controller: _controller,
                    decoration: InputDecoration(
                      hintText: "Enter IP Address",
                      border: OutlineInputBorder(
                        borderRadius: BorderRadius.all(Radius.circular(30)),
                      ),
                    ),
                  ),
                  Positioned(
                    right: 6,
                    top: 6,
                    child: ElevatedButton(
                      onPressed: () async {
                        if (_controller.text.isNotEmpty) {
                          final (checker, updatedChannel) =
                              await connectChannel(_controller.text);
                          context.read<TextProvider>().setChannel(
                            updatedChannel,
                          );
                          context.read<TextProvider>().setChannelChecker(
                            checker,
                          );
                          if (context.read<TextProvider>().checker) {
                            ScaffoldMessenger.of(context).showSnackBar(
                              SnackBar(
                                duration: Duration(milliseconds: 1500),
                                backgroundColor: Colors.lightGreenAccent,
                                content: Center(
                                  child: Text(
                                    "IP Connected",
                                    style: TextStyle(
                                      color: Colors.deepOrangeAccent,
                                    ),
                                  ),
                                ),
                              ),
                            );
                          } else {
                            ScaffoldMessenger.of(context).showSnackBar(
                              SnackBar(
                                duration: Duration(milliseconds: 1500),
                                backgroundColor: Colors.orangeAccent,
                                content: Center(
                                  child: Text(
                                    "IP Did not Connect, Check IP and Retry",
                                    style: TextStyle(
                                      fontWeight: FontWeight.bold,
                                    ),
                                  ),
                                ),
                              ),
                            );
                          }
                        } else {
                          ScaffoldMessenger.of(context).showSnackBar(
                            SnackBar(
                              backgroundColor: Colors.orangeAccent,
                              content: Center(child: Text("Enter IP Address")),
                              duration: Duration(milliseconds: 1500),
                            ),
                          );
                        }
                      },
                      child: Text(
                        "ConnectIP",
                        style: TextStyle(fontFamily: "Caveat"),
                      ),
                    ),
                  ),
                ],
              ),
            ),
            SizedBox(height: 3),
            ElevatedButton(
              style: ButtonStyle(
                surfaceTintColor: WidgetStatePropertyAll(
                  Colors.lightGreenAccent,
                ),
              ),
              onPressed: () {
                if (context.read<TextProvider>().checker) {
                  context.read<TextProvider>().setText(_controller.text);
                  Navigator.of(
                    context,
                  ).push(MaterialPageRoute(builder: (_) => Connectionpage()));
                } else {
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(
                      backgroundColor: Colors.orangeAccent,
                      content: Center(child: Text("Connect to IP.")),
                      duration: Duration(milliseconds: 1500),
                    ),
                  );
                }
              },
              child: Text("Proceed", style: TextStyle(fontFamily: "Bungee")),
            ),
          ],
        ),
      ),
    );
  }
}
