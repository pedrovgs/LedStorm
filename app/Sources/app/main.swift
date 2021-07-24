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
  @State var lightning1Color = Color.white
  @State var lightning2Color = Color.white
  var body: some View {
    VStack {
      Spacer().frame(height: 150)
      LightningColorPicker(lightningNumber: 1, selectedColor: lightning1Color) {
        lightning1Color = $0
      }
      Spacer().frame(height: 50)
      LightningColorPicker(lightningNumber: 2, selectedColor: lightning2Color) {
        lightning2Color = $0
      }
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
