import Foundation

class LedStorm {
  let lightning1: Lightning
  let lightning2: Lightning
  init(
    lightning1: Lightning,
    lightning2: Lightning
  ) {
    self.lightning1 = lightning1
    self.lightning2 = lightning2
  }
}

struct Lightning {
  let color: LightningColor
}

struct LightningColor: Hashable {
  static let white = LightningColor(red: 255, green: 255, blue: 255)
  let red: Int
  let green: Int
  let blue: Int
}
