import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_gauges/gauges.dart';

class DustLevel extends StatefulWidget {
  const DustLevel({super.key});

  @override
  State<DustLevel> createState() => _DustLevelState();
}

class _DustLevelState extends State<DustLevel> {
  @override
  Widget build(BuildContext context) {
    return SfRadialGauge(
      title: const GaugeTitle(
        text: 'Dust Level',
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
            GaugeRange(
                startValue: 0, endValue: 33, color: Colors.brown.shade300),
            GaugeRange(
                startValue: 33, endValue: 66, color: Colors.brown.shade400),
            GaugeRange(
                startValue: 66, endValue: 100, color: Colors.brown.shade500),
          ],
          pointers: <GaugePointer>[
            NeedlePointer(value: 48.0),
          ],
          annotations: <GaugeAnnotation>[
            GaugeAnnotation(
                widget: Container(
                  child: Text(
                    '48.0',
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
