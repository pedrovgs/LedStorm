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
  @State var lightning1Color = LightningColor.white
  @State var lightning2Color = LightningColor.white
  var body: some View {
    VStack {
      Spacer().frame(height: 150)
      LightningColorPicker(lightningNumber: 1, selectedColor: lightning1Color) {
        print("Lightning 1 color selected = \($0)")
        lightning1Color = $0
      }
      Spacer().frame(height: 50)
      LightningColorPicker(lightningNumber: 2, selectedColor: lightning2Color) {
        print("Lightning 2 color selected = \($0)")
        lightning2Color = $0
      }
      Spacer()
      HStack {
        Button(
          action: {
            let storm = composeStormFromState(lightning1Color, lightning2Color)
            sendLightningRequest(storm: storm)
          },
          label: {
            Text("⚡️").font(.system(size: 160))
          }
        ).buttonStyle(TransparentButtonStyle())
        Button(
          action: {
            let storm = composeStormFromState(lightning1Color, lightning2Color)
            sendSwitchLampOnRequest(storm: storm)
          },
          label: {
            Text("💡").font(.system(size: 160))
          }
        ).buttonStyle(TransparentButtonStyle())
      }
    }
  }
}

private func composeStormFromState(
  _ lightning1Color: LightningColor,
  _ lightning2Color: LightningColor
) -> LedStorm {
  let lightning1 = Lightning(color: LightningColor(
    red: lightning1Color.red,
    green: lightning1Color.green,
    blue: lightning1Color.blue
  ))
  let lightning2 = Lightning(color: LightningColor(
    red: lightning2Color.red,
    green: lightning2Color.green,
    blue: lightning2Color.blue
  ))
  return LedStorm(
    lightning1: lightning1,
    lightning2: lightning2
  )
}

LedStormApp.main()
