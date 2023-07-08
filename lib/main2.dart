


// import 'package:flutter/material.dart';
// import 'package:syncfusion_flutter_gauges/gauges.dart';

// void main() {
//   runApp(DashboardPage());
// }

// class DashboardPage extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       title: "eare",
//       home: Scaffold(
//         appBar: AppBar(
//           title: Text('Dashboard'),
//         ),
//         body: GridView.count(
//           shrinkWrap: true,
//           crossAxisCount: 2,
//           // padding: EdgeInsets.all(16),
//           children: [
//             buildGaugeCard(
//               'Gauge 1',
//               SfRadialGauge(
//                 axes: <RadialAxis>[
//                   RadialAxis(
//                     minimum: 0,
//                     maximum: 150,
//                     ranges: <GaugeRange>[
//                       GaugeRange(
//                           startValue: 0, endValue: 50, color: Colors.green),
//                       GaugeRange(
//                           startValue: 50, endValue: 100, color: Colors.orange),
//                       GaugeRange(
//                           startValue: 100, endValue: 150, color: Colors.red),
//                     ],
//                     pointers: <GaugePointer>[
//                       NeedlePointer(value: 90),
//                     ],
//                     annotations: <GaugeAnnotation>[
//                       GaugeAnnotation(
//                         widget: Container(
//                           child: Text(
//                             '90.0',
//                             style: TextStyle(
//                                 fontSize: 25, fontWeight: FontWeight.bold),
//                           ),
//                         ),
//                         angle: 90,
//                         positionFactor: 0.5,
//                       ),
//                     ],
//                   )
//                 ],
//               ),
//             ),
//             buildGaugeCard(
//               'Gauge 2',
//               SfRadialGauge(axes: <RadialAxis>[
//                 RadialAxis(
//                   minimum: 0,
//                   maximum: 150,
//                   ranges: <GaugeRange>[
//                     GaugeRange(
//                         startValue: 0, endValue: 50, color: Colors.green),
//                     GaugeRange(
//                         startValue: 50, endValue: 100, color: Colors.orange),
//                     GaugeRange(
//                         startValue: 100, endValue: 150, color: Colors.red),
//                   ],
//                   pointers: <GaugePointer>[
//                     NeedlePointer(value: 90),
//                   ],
//                   annotations: <GaugeAnnotation>[
//                     GaugeAnnotation(
//                       widget: Container(
//                         child: Text(
//                           '90.0',
//                           style: TextStyle(
//                               fontSize: 25, fontWeight: FontWeight.bold),
//                         ),
//                       ),
//                       angle: 90,
//                       positionFactor: 0.5,
//                     ),
//                   ],
//                 )
//               ]
//                   // Gauge 2 configuration...
//                   ),
//             ),
//             buildGaugeCard(
//               'Gauge 3',
//               SfRadialGauge(
//                   // Gauge 3 configuration...
//                   ),
//             ),
//             buildGaugeCard(
//               'Linear Gauge',
//               SfLinearGauge(
//                   // Linear gauge configuration...
//                   ),
//             ),
//           ],
//         ),
//       ),
//     );
//   }

//   Widget buildGaugeCard(String title, Widget gaugeWidget) {
//     return Card(
//       // margin: EdgeInsets.only(bottom: 50),
//       elevation: 4,
//       shape: RoundedRectangleBorder(
//         borderRadius: BorderRadius.circular(8),
//       ),
//       child: Column(
//         mainAxisAlignment: MainAxisAlignment.start,
//         children: [
//           Padding(
//             padding: const EdgeInsets.all(2.0),
//             child: Text(
//               title,
//               style: TextStyle(
//                 fontSize: 20,
//                 fontWeight: FontWeight.bold,
//               ),
//             ),
//           ),
//           // SizedBox(height: 16),
//           Container(height: 150, width: 150, child: gaugeWidget),
//         ],
//       ),
//     );
//   }
// }
