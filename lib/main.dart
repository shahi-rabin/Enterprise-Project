import 'package:flutter/material.dart';
import 'package:smart_pole/dust_level.dart';
import 'package:smart_pole/humidity.dart';
import 'package:smart_pole/temperature.dart';
import 'ldr.dart';
import 'package:syncfusion_flutter_gauges/gauges.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Smart Pole IOT",
      debugShowCheckedModeBanner: false,
      theme: ThemeData(useMaterial3: true, primarySwatch: Colors.blue),
      home: Scaffold(
        appBar: AppBar(
          title: const Text(
            "Smart Pole",
            style: TextStyle(
              color: Colors.white,
              fontWeight: FontWeight.bold,
            ),
          ),
          centerTitle: true,
          backgroundColor: Colors.blue,
        ),
        body: SingleChildScrollView(
          child: Column(
            children: <Widget>[
              Row(
                children: <Widget>[
                  Expanded(
                    child: Container(
                      child: Temperature(),
                    ),
                  ),
                  Expanded(
                    child: Humidity(),
                  )
                ],
              ),
              Row(
                children: <Widget>[
                  Expanded(
                    child: DustLevel(),
                  ),
                  Expanded(child: Ldr())
                ],
              )
            ],
          ),
        ),
      ),
    );
  }
}
