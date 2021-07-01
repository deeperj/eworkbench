import QtQuick 2.12
import QtCharts 2.0


/*
import QtQuick 2.12
import QtQuick.Controls 2.5
import QtCharts 2.15

  Component.onCompleted: {
    for (var i = 0; i < daysCount; i++) {
      jackSeries.append( daysNumbers[i], jackApples[i] )
      jillSeries.append( daysNumbers[i], jillApples[i] )
    }
  }
*/
//  NavigationStack {
Item {
    id: lineSeries

    readonly property var daysNumbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    readonly property int daysCount: lineSeries.daysNumbers.length
    readonly property var jackApples: [2, 2, 3, 2, 4, 5, 3, 3, 2, 1]
    readonly property var jillApples: [1, 2, 2, 3, 2, 3, 2, 1, 1, 2]

    readonly property var jackAndJillResults: lineSeries.jackApples.concat(
                                                  lineSeries.jillApples)

    readonly property color jackColor: "lightsalmon"
    readonly property color jillColor: "lightskyblue"
    readonly property string jackTitle: "Apples count Jack ate per day"
    readonly property string jillTitle: "Apples count Jill ate per day"

    ChartView {
        title: "Apples eaten per day"
        anchors.fill: parent
        antialiasing: true
        legend.alignment: Qt.AlignBottom

        // Define x-axis to be used with the series instead of default one
        ValueAxis {
            id: xAxis
            tickCount: 10
            labelFormat: "%.0f"
            titleText: "Day number"
        }

        ValueAxis {
            id: yAxis
            titleText: "Amount of apples eaten"
        }

        LineSeries {
            id: jackSeries
            name: jackTitle
            color: jackColor
            axisX: xAxis
            axisY: yAxis
            width: 5
            capStyle: Qt.RoundCap
            pointsVisible: true
        }

        LineSeries {
            id: jillSeries
            name: jillTitle
            color: jillColor
            axisX: xAxis
            axisY: yAxis
            width: 5
            capStyle: Qt.RoundCap
            pointsVisible: true
        }
    }

    Connections {
        target: lineSeries
        onFocusChanged: {
            // Here we use ES6 spread operator "..."
            yAxis.max = Math.max.apply(Math, lineSeries.jackAndJillResults)+1
            yAxis.min = Math.min.apply(Math, lineSeries.jackAndJillResults)-1
            xAxis.min = 0
            xAxis.max = 10
            //property int maxApples: Math.max.apply(Math, lineSeries.jackAndJillResults)
            print("hello" + Math.max.apply(Math, lineSeries.jackAndJillResults))
            for (var i = 0; i < lineSeries.daysCount; i++) {
                jackSeries.append(lineSeries.daysNumbers[i], jackApples[i])
                jillSeries.append(lineSeries.daysNumbers[i], jillApples[i])
            }
        }
    }
} //  }

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}
}
##^##*/

