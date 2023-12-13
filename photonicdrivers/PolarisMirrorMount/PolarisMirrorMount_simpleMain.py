from PolarisMirrorMount import Polaris

def main():
    kpz101SerialNoX = "29252886"
    kpz101SerialNoY = "29252886"
    polaris = Polaris(kpz101SerialNoX, kpz101SerialNoY)
    print(polaris.Piezo.getMaxVoltage())
    print('done')

if __name__ == "__main__":
    main()