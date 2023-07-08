import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_gauges/gauges.dart';

class Humidity extends StatefulWidget {
  const Humidity({super.key});

  @override
  State<Humidity> createState() => _HumidityState();
}

class _HumidityState extends State<Humidity> {
  @override
  Widget build(BuildContext context) {
    return Column(      
      children: [        
        SfLinearGauge(
          
          ranges: [
            LinearGaugeRange(
              startValue: 0,
              endValue: 50,
            ),
          ],
          markerPointers: [
            LinearShapePointer(
              value: 50,
            ),
          ],
          barPointers: [
            LinearBarPointer(value: 80),
          ],
        )

      ],
    );
  }
}
