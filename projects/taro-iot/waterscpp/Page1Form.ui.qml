import QtQuick 2.12
import QtQuick.Controls 2.5

Page {
    id: page
    width: 600
    height: 400
    property variant toggle: false
    header: Label {
        text: qsTr("Pump 1")
        font.pixelSize: Qt.application.font.pixelSize * 2
        padding: 10
    }

    Rectangle {
        id: rect2
        anchors.centerIn: parent
        width: parent.width / 3
        height: rect2.width
        border.color: "lightsteelblue"
        border.width: 6
        radius: 8

        MouseArea {
            id: mouseArea
            anchors.fill: parent
        }
    }

    Connections {
        target: mouseArea
        onClicked: {
            print("h3llo")
            page.toggle = !page.toggle
            page.state = page.toggle ? "State1" : ""
        }
    }
    states: [
        State {
            name: "State1"
            PropertyChanges {
                target: rect2
                color: "#33e148"
            }
        }
    ]
}
