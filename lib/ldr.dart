import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_gauges/gauges.dart';

class Ldr extends StatefulWidget {
  const Ldr({super.key});

  @override
  State<Ldr> createState() => _LdrState();
}

class _LdrState extends State<Ldr> {
  @override
  Widget build(BuildContext context) {
    return SfRadialGauge(
      title: const GaugeTitle(
        text: 'LDR',
        textStyle: TextStyle(
          fontSize: 25.0,
          fontWeight: FontWeight.bold,
        ),
      ),
      axes: <RadialAxis>[
        RadialAxis(
          minimum: 0,
          maximum: 100,
          ranges: <GaugeRange>[
            GaugeRange(startValue: 0, endValue: 33, color: Colors.green),
            GaugeRange(startValue: 33, endValue: 66, color: Colors.orange),
            GaugeRange(startValue: 66, endValue: 100, color: Colors.red),
          ],
          pointers: <GaugePointer>[
            NeedlePointer(value: 80),
          ],
          annotations: <GaugeAnnotation>[
            GaugeAnnotation(
                widget: Container(
                  child: Text(
                    '80.0',
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
