import QtQuick 2.12
import QtQuick.Controls 2.5
import Felgo 3.0

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: qsTr("Tabs")

    SwipeView {
        id: swipeView
        anchors.fill: parent
        currentIndex: tabBar.currentIndex

        Page1Form {
        }

        Page2Form {
        }
        Page{
            JsonListModel {
                id: jsonModel1
                //source: "http://localhost:8090/WeatherForecast"
                // All books in the store object
                //query: "$.store.book[*]"
            }
            ListView {
               model: jsonModel1.model
               delegate: Component {
                   Text {
                       // Can be any of the JSON properties: model.author, model.price, etc.
                       text: model.summary
                       onActiveFocusChanged: getJson()
                   }
               }
            }
        }
    }
    function getJson() {
          var httpRequest = new XMLHttpRequest();
          // the 3rd parameter is the asynchronous flag, see here: http://www.w3.org/TR/XMLHttpRequest/#the-open-method
          httpRequest.open("GET", "http://localhost:8090/WeatherForecast", true);
          httpRequest.onreadystatechange = function() {
              if (httpRequest.readyState == httpRequest.DONE) {

                  var serverResponse = httpRequest.responseText;
                  console.debug("httpRequest result:", serverResponse);

                  if(!serverResponse) {
                      nativeUtils.displayMessageBox("Failed to load levels from server");
                      return;
                  }

                  // example result: [{"lastModificationTime":"2012-05-06T23:06:41+02:00","levelName":"Test","levelId":1}]
                  jsonModel1.source = JSON.parse(serverResponse);

              }
          }
    }
    footer: TabBar {
        id: tabBar
        currentIndex: swipeView.currentIndex

        TabButton {
            text: qsTr("Page 1")
        }
        TabButton {
            text: qsTr("Page 2")
        }
    }
}

