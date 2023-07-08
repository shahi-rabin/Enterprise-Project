import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_gauges/gauges.dart';

class Temperature extends StatefulWidget {
  const Temperature({super.key});

  @override
  State<Temperature> createState() => _TemperatureState();
}

class _TemperatureState extends State<Temperature> {
  @override
  Widget build(BuildContext context) {
    return SfRadialGauge(
      title: const GaugeTitle(
        text: 'Temperature',
        textStyle: TextStyle(
          fontSize: 25.0,
          fontWeight: FontWeight.bold,
        ),
      ),
      axes: <RadialAxis>[
        RadialAxis(
          minimum: 0,
          maximum: 75,
          ranges: <GaugeRange>[
            GaugeRange(startValue: 0, endValue: 25, color: Colors.blue[400]),
            GaugeRange(startValue: 25, endValue: 50, color: Colors.orange),
            GaugeRange(startValue: 50, endValue: 75, color: Colors.red),
          ],
          pointers: <GaugePointer>[
            NeedlePointer(value: 25),
          ],
          annotations: <GaugeAnnotation>[
            GaugeAnnotation(
                widget: Container(
                  child: Text(
                    '25.0',
                    style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                  ),
                ),
                angle: 90,
                positionFactor: 0.7),
          ],
        )
      ],
    );
  }
}
