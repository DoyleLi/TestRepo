DB_P = "buildbot"

WORKER_P = {
    "ubuntu_1804_x64_01" : "fc4239f96745cb1417a70aa06e84f699", # nnlocl072
    "ubuntu_1804_x64_02" : "e42d1adc3955d220e1b2aec96ebbb81e", # nnlocl093
    "ubuntu_1804_x64_03" : "dda1da44f7164a291c9c646afd3935a0", # nnlocl074
    "ubuntu_1804_x64_04" : "ee747cc88ddb78a9097e66250e260033", # nnlocl108
    "ubuntu_1804_x64_05" : "0c932e32e2f18c78d98fa03699553bf1", # nnlocl109
    "ubuntu_1804_x64_06" : "1c1255a92e3b2787e51d3a6af2f60b3e", # nnlocl110
    "ubuntu_1804_x64_07" : "3ac0d29fb353867ffb746ef8868d230a", # nnlocl073
    "ubuntu_1804_x64_08" : "3d97e1bf71f81b5e03469443a88a8271", # nnlocl094
    "ubuntu_1804_x64_09" : "c51a927d7bf048c354b0c848a62ab837", # nnlocl112
    "ubuntu_1804_x64_10" : "f61194d983ad1daa94ab2c3de04b4881", # nnlocl114
    "ubuntu_1804_x64_11" : "f9d47c1c53dea494c8c0725bf6354325", # nnlocl115
    "ubuntu_1804_x64_12" : "d82ae924091415cb15cb47340b13e074", # nnlocl111
    "ubuntu_1804_x64_13" : "632ca4abaff0958c4ae98e9cb860b19b", # nnlocl009
    "ubuntu_1804_x64_14" : "934f266b69bd3bdec51abbfb2dcc0476", # nnlocl076
    "ubuntu_1804_x64_15" : "2b426c079c8f751a453011d084c07e13", # nnlocl104
    "ubuntu_1804_x64_16" : "a4afdd1dcadf5764cce12c44fe1fa985", # nnlocl105
    "ubuntu_1804_x64_17" : "22f6bdbb721eafafb179c2840dc8edce", # nnlocl106
    "ubuntu_1804_x64_18" : "f77c3f31d0a73a7d240b09913c35dafb", # nnlocl107
    "ubuntu_1804_x64_19" : "7458374f787b25d42e4145a1c569dadf", # TBD
    "ubuntu_1804_x64_20" : "26300f8ade7b275a0981502eeaf5a89d", # TBD
    "ubuntu_1804_x64_21" : "aba7ed2f2e9dcb88cf3a725a880a19f1", # TBD
    "ubuntu_1804_x64_22" : "31ab508c9f37108fc7c09ac309ae7115", # TBD
    "ubuntu_1804_x64_23" : "509fe748870d6783805f0fbfb5e0ede0", # TBD
    "ubuntu_1804_x64_24" : "36845caf48925f31681972c1d7e9c2c9", # TBD
    "ubuntu_1804_x64_25" : "6acd52adfc1a6f887a1650d693f8536f", # TBD
    "ubuntu_1804_x64_26" : "7d6fca1d879af017f1fea3e05e20fc3c", # TBD
    "ubuntu_1804_x64_27" : "48f7c40ef042cb9ba392045014b7df4b", # TBD
    "ubuntu_1804_x64_28" : "1a59620a474465b7d98b36f8a24cc977", # TBD
    "ubuntu_1804_x64_29" : "9ae0921ab8064f04df537abb6d35f8c0", # TBD
    "ubuntu_1804_x64_30" : "4eb99b271d1714c9befd1a0533f3d3f6", # TBD
    "ubuntu_1804_x64_31" : "3ff4741e49dd9a36e123502fcd85ff91", # TBD
    "ubuntu_1804_x64_32" : "665b3a18ae692446aef9ea6ccff65dfd", # TBD
    "ubuntu_1804_x64_33" : "0e82b3b0b507f1bc6d619253675ab02e", # TBD
    "ubuntu_1804_x64_34" : "0df9e2690b893e61c34350ef4aafff9e", # TBD
    "ubuntu_1804_x64_shz" : "3745ebfa40208e383f654f9d491bf507", # ubuntu test pc in shz lab
    "sycl_rh74_x64_01" : "2218d58294498cc5cc511e95cedb3953", # nnlocl126
    "sycl_rh74_x64_02" : "66493d600b561f5591e120dafa963efd", # TBD
    "sycl_rh74_x64_03" : "3b0852b1a3a44007daaa02236dc6ec84", # TBD
    "sycl_rh74_x64_04" : "61bf2e5c9db2217d6148df68a405b05e", # TBD
    "win_x64_test" : "7ec09ca90eb460a9e5bb067cf7031dde", #testWin 
    "win_2k19_x64_01" : "d3787a183a89c478e93abbdba85ca6c8", #nnvocl146
    "win_2k19_x64_02" : "60e66983d326219106797b0f6870b7ff", #nnlocl143
    "win_2k19_x64_03" : "8ce1d136fa8a483a9e472f00b6de9dec", #nnlocl117
    "win_2k19_x64_04" : "8c92714f69edbe348b6c37182c66b657", #nnlocl144
    "win_2k19_x64_05" : "210b57ad5bdd666ecad95ff103c1949d", #nnlocl
    "win_2k19_x64_06" : "e24310c050ebd65598f084abe2d65ed2", #nnlocl
    "win_2k19_x64_07" : "915165f7a2a3d21eabc5c58ef4e54782", #nnlocl
    "win_2k19_x64_08" : "e093c65e7ec3388807d6a9b78d0d9a1c", #nnlocl
    "win_2k19_x64_09" : "b4881d97a9494cbf018fe2f4f9589035", #nnlocl
    "win_2k19_x64_10" : "d362d409af82c6bb23e01dbdfddc2e18", #nnlocl
    "win_2k19_x64_11" : "c15585552225586c2e8d6f3b24b8ff9e", #nnlocl
    "win_2k19_x64_12" : "efcd985fa193a297cb4e329b7489f05e", #nnlocl
    "win_2k19_x64_13" : "6872cf66d2c75ac9023292a7db97783d", #nnlocl
    "win_2k19_x64_14" : "c980e326b4ed38eebfe706bcd09fff85", #nnlocl
}

GITHUB = {
    #for github user DoyleLi
    "change_hook" : "d62cf0ff6b59beffbcd6e737557f8ebd",
    "tk" : "bf8d9c8a15fbafccbb4b171ec192f606d50eed0b",
    "ci" : "9c3c5c967d9c20c314a1",
    "cs" : "85c3b818f34d64bb490b5ba174b243965856c574"
}

