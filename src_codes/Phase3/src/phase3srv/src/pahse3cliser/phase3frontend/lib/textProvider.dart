import 'package:flutter/material.dart';
import 'package:web_socket_channel/web_socket_channel.dart';

class TextProvider extends ChangeNotifier {
  String text = "";
  WebSocketChannel? channel;
  bool checker=false;

  void setText(String newText) {
    text = newText;
    notifyListeners();
  }

  void setChannel(WebSocketChannel channelUpdated) {
    channel = channelUpdated;
    notifyListeners();
  }

  void setChannelChecker(bool checkerUpdated){
    checker=checkerUpdated;
    notifyListeners();
  }
}

