import toptica.lasersdk.dlcpro.v3_0_1 as toptica

laser = toptica.DLCpro(toptica.NetworkConnection('10.209.67.103'))
laser.open()
laser.close()
    