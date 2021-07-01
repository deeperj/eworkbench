#include <iostream>
#include <thread>
#include <chrono>
#include <asio.hpp>
#include <asio/ts/buffer.hpp>
#include <asio/ts/internet.hpp>

using std::cout;
using std::vector;
using std::string;
using std::endl;


int main(void){

  asio::error_code ec;

  asio::io_context context;

  asio::ip::tcp::endpoint endpoint(asio::ip::make_address("127.0.0.1", ec), 8090);

  asio::ip::tcp::socket socket(context);

  socket.connect(endpoint, ec);

  if(!ec){
    cout << "Connected!" << endl;
  }else{
    cout << "Failed to connect; " << ec.message() << endl;
  }
  if(socket.is_open()){
    string sReq = 
      "GET /WeatherForecast HTTP/1.1\r\n"
      "HOST: localhost:8090\r\n"
      "Connection: close\r\n\r\n";

      socket.write_some(asio::buffer(sReq.data(), sReq.size()), ec);

      socket.wait(socket.wait_read);

      size_t bytes = socket.available();
      cout << "Bytes available = " << bytes << endl;

      if(bytes>0){
        vector<char> vBuf(bytes);
        socket.read_some(asio::buffer(vBuf.data(),vBuf.size()),ec);
        for(auto c: vBuf){
          cout << c;
        }
      }
  }
  return 0;
}
