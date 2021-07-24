import Foundation
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
      LightningColorPicker(lightningNumber: 1)
      Spacer()
      LightningColorPicker(lightningNumber: 2)
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

LedStormApp.main()
