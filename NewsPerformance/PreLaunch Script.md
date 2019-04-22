xcodebuild -project /Users/jayce/Jayce-iOSPerformance/NewsPerformance/iOS-Tagent/WebDriverAgent.xcodeproj   -scheme WebDriverAgentRunner -destination "id=f94ae345c82dcef7a575b84db7e95aac05d85d90" test

 iproxy 8100 8100

 python -m airtest run /Users/jayce/Jayce-iOSPerformance/Case/NetEase/Launch.air  --device iOS:///127.0.0.1:8100 --log  /Users/jayce/Desktop/Airtest

 python -m airtest run /Users/jayce/Jayce-iOSPerformance/Case/NetEase/Article.air  --device iOS:///127.0.0.1:8100 --log  /Users/jayce/Desktop/Airtest

 python -m airtest run /Users/jayce/Jayce-iOSPerformance/Case/NetEase/Pictures.air  --device iOS:///127.0.0.1:8100 --log  /Users/jayce/Desktop/Airtest

 python -m airtest run /Users/jayce/Jayce-iOSPerformance/Case/NetEase/Refresh-toutiao.air  --device iOS:///127.0.0.1:8100 --log  /Users/jayce/Desktop/Airtest

 python -m airtest run /Users/jayce/Jayce-iOSPerformance/Case/NetEase/Refresh-VideoTab.air  --device iOS:///127.0.0.1:8100 --log  /Users/jayce/Desktop/Airtest

 python -m airtest run /Users/jayce/Jayce-iOSPerformance/Case/NetEase/VideoArticle.air  --device iOS:///127.0.0.1:8100 --log  /Users/jayce/Desktop/Airtest
 
 python -m airtest run /Users/jayce/Jayce-iOSPerformance/Case/NetEase/VideoPlay.air  --device iOS:///127.0.0.1:8100 --log  /Users/jayce/Desktop/Airtest