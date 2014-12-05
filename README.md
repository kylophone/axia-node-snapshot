axia-node-snapshot
==================

Get a snapshot of internal state of an AXIA node. Reverse engineered LWRP. Parses responses and returns the data encoded as JSON (prints to stdout.) There's lots of data available in each node, as you can see in the example below. Takes one argument: Axia Node IP. 

```bash
python axianodesnapshot.py 10.27.37.121
```

```bash
{
    "destination": {
        "1": {
            "ADDR": "239.192.0.5",
            "DST": "1",
            "NAME": "Homer",
            "NCHN": "2",
            "OUGN": "0",
            "VMOD": "*"
        },
        "2": {
            "ADDR": "239.192.0.6",
            "DST": "2",
            "NAME": "DST 2",
            "NCHN": "2",
            "OUGN": "0",
            "VMOD": "*"
        },
        "3": {
            "ADDR": "239.192.0.7",
            "DST": "3",
            "NAME": "DST 3",
            "NCHN": "2",
            "OUGN": "0",
            "VMOD": "*"
        },
        "4": {
            "ADDR": "239.192.0.8",
            "DST": "4",
            "NAME": "DST 4",
            "NCHN": "2",
            "OUGN": "0",
            "VMOD": "*"
        },
        "5": {
            "ADDR": "239.192.0.5",
            "DST": "5",
            "NAME": "DST 5",
            "NCHN": "0",
            "OUGN": "0",
            "VMOD": "*"
        },
        "6": {
            "ADDR": "239.192.0.6",
            "DST": "6",
            "NAME": "DST 6",
            "NCHN": "0",
            "OUGN": null,
            "VMOD": null
        },
        "7": {
            "ADDR": "239.192.0.7",
            "DST": "7",
            "NAME": "DST 7",
            "NCHN": "0",
            "OUGN": null,
            "VMOD": null
        },
        "8": {
            "ADDR": "239.192.0.8",
            "DST": "8",
            "NAME": "DST 8",
            "NCHN": "0",
            "OUGN": null,
            "VMOD": null
        }
    },
    "gpio": {
        "1": {
            "GPI": "hhhhh",
            "GPIO": "1",
            "GPO": "hhhhh",
            "SRCA": "2"
        },
        "2": {
            "GPI": "hhhhh",
            "GPIO": "2",
            "GPO": "hhhhh",
            "SRCA": "12"
        }
    },
    "node": {
        "ADIP": "239.192.255.3",
        "AESSYNCE": "0",
        "AESSYNC_OUT": "0",
        "AESSYNC_PRI": "0",
        "AESTX_AUTO": "0",
        "DEVN": "axiaunode.combo",
        "IPCLK_ADDR": "239.192.255.2",
        "LWCLK_ADDR": "239.192.255.1",
        "LWCLK_MODE": "1",
        "LWCLK_PRIO": "3",
        "LWS_802_1Q_PRIO": "7",
        "LWS_802_1p_TAGE": "0",
        "LWS_802_1p_VLAN": "0",
        "LWS_IP_TOS": "136",
        "MODEL": "Mixed Signal I/O",
        "NDST": "8",
        "NGPI": "2",
        "NGPO": "2",
        "NID": "198/8",
        "NSRC": "8",
        "PRODUCT": "Axia Node",
        "RTP_802_1Q_PRIO": "7",
        "RTP_802_1p_TAGE": "0",
        "RTP_802_1p_VLAN": "0",
        "RTP_IP_TOS": "64",
        "RXBUFF": "100",
        "SVER": "1.0.7a",
        "address": "10.27.37.121",
        "gateway": "10.27.1.1",
        "hostname": "Node-198-8",
        "netmask": "255.255.255.0"
    },
    "source": {
        "1": {
            "AESM": null,
            "INGN": "440",
            "IO": "M",
            "NCHN": "2",
            "PHPW": "1",
            "PSNM": "CSF TEST",
            "RTPA": "239.192.0.1",
            "RTPE": "1",
            "RTPP": "12",
            "SHAB": "1",
            "SRC": "1"
        },
        "2": {
            "AESM": null,
            "INGN": "0",
            "IO": null,
            "NCHN": "2",
            "PHPW": null,
            "PSNM": "SRC 2",
            "RTPA": "239.192.0.2",
            "RTPE": "1",
            "RTPP": "12",
            "SHAB": "0",
            "SRC": "2"
        },
        "3": {
            "AESM": null,
            "INGN": "0",
            "IO": null,
            "NCHN": "2",
            "PHPW": null,
            "PSNM": "SRC 3",
            "RTPA": "239.192.0.3",
            "RTPE": "1",
            "RTPP": "12",
            "SHAB": "0",
            "SRC": "3"
        },
        "4": {
            "AESM": "1",
            "INGN": "0",
            "IO": null,
            "NCHN": "2",
            "PHPW": null,
            "PSNM": "SRC 4",
            "RTPA": "239.192.0.4",
            "RTPE": "1",
            "RTPP": "12",
            "SHAB": "0",
            "SRC": "4"
        },
        "5": {
            "AESM": null,
            "INGN": "0",
            "IO": null,
            "NCHN": "0",
            "PHPW": null,
            "PSNM": "SRC 5",
            "RTPA": "239.192.77.173",
            "RTPE": "0",
            "RTPP": "12",
            "SHAB": "0",
            "SRC": "5"
        },
        "6": {
            "AESM": null,
            "INGN": null,
            "IO": null,
            "NCHN": "0",
            "PHPW": null,
            "PSNM": "SRC 6",
            "RTPA": "239.192.77.174",
            "RTPE": "0",
            "RTPP": "12",
            "SHAB": null,
            "SRC": "6"
        },
        "7": {
            "AESM": null,
            "INGN": null,
            "IO": null,
            "NCHN": "0",
            "PHPW": null,
            "PSNM": "SRC 7",
            "RTPA": "239.192.77.175",
            "RTPE": "0",
            "RTPP": "12",
            "SHAB": null,
            "SRC": "7"
        },
        "8": {
            "AESM": null,
            "INGN": null,
            "IO": null,
            "NCHN": "0",
            "PHPW": null,
            "PSNM": "SRC 8",
            "RTPA": "239.192.77.176",
            "RTPE": "0",
            "RTPP": "12",
            "SHAB": null,
            "SRC": "8"
        }
    }
}
```
