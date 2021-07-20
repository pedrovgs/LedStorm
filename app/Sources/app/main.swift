import Foundation
import JavaScriptKit
import TokamakDOM

struct LedStormApp: App {
  var body: some Scene {
    WindowGroup("Tokamak App") {
      LedStormView()
    }
  }
}

struct LedStormView: View {
  @State private var count: Int = 0
  var body: some View {
    VStack {
      Spacer()
      Button(
        action: {
          sendLightningRequest()
        },
        label: {
          Text("⚡️").font(.system(size: 160))
        }
      ).buttonStyle(TransparentButtonStyle())
    }
  }
}

struct TransparentButtonStyle: ButtonStyle {
  func makeBody(configuration: Configuration) -> some View {
    let isPressed = configuration.isPressed
    return configuration
      .label.background(isPressed ? Color.buttonPressed : Color.clear)
  }
}

extension Color {
  static let buttonPressed = Color(red: 0.29, green: 0.29, blue: 0.29, opacity: 1.0)
}

LedStormApp.main()

private func sendLightningRequest() {
  print("CLICK")
  let url = "http://raspberrypi.local"
  let fetchPromise: JSPromise = fetch(url)
  fetchPromise.then { value -> String in
    print("Value = \(value)")
    return ""
  } failure: { error -> String in
    print("Value = \(error)")
    return ""
  }
}

func fetch(_ url: String) -> JSPromise {
  let _jsFetch = JSObject.global.fetch.function!
  return JSPromise(_jsFetch(url).object!)!
}
