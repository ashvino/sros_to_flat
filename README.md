**Example of sros-to-flat.py**

Script to generate flat config for NOKIA SROS from an existing SROS indented config file.
SROS config file hierarchies are indented by 4 spaces.

Script written in python3


```
Example:


$ python3 sros-to-flat.py sample-sros.conf\n
/configure router ospf asbr
/configure router ospf reference-bandwidth 1000000000
/configure router ospf external-db-overflow 5000 3600
/configure router ospf overload-on-boot timeout 300
/configure router ospf traffic-engineering
/configure router ospf timers spf-wait 5000 200 200
/configure router ospf timers lsa-generate 5000 50 50
/configure router ospf timers lsa-arrival 0
/configure router ospf export static-to-ospf
/configure router ospf graceful-restart
/configure router ospf loopfree-alternate
/configure router ospf area 0.0.0.0 interface "system" no shutdown
/configure router ospf area 0.0.0.0 interface core_Test authentication-type message-digest
/configure router ospf area 0.0.0.0 interface core_Test message-digest-key 1 md5 core-interface-md5
/configure router ospf area 0.0.0.0 interface core_Test no shutdown
/configure router ospf area 0.0.0.0 interface core_Test1 authentication-type message-digest
/configure router ospf area 0.0.0.0 interface core_Test1 message-digest-key 1 md5 core-interface-md5
/configure router ospf area 0.0.0.0 interface core_Test1 no shutdown
/configure router ospf area 0.0.0.0 interface core_Test2 interface-type point-to-point
/configure router ospf area 0.0.0.0 interface core_Test2 metric 200
/configure router ospf area 0.0.0.0 interface core_Test2 authentication-type message-digest
/configure router ospf area 0.0.0.0 interface core_Test2 message-digest-key 1 md5 Test_MD5
/configure router ospf area 0.0.0.0 interface core_Test2 no shutdown
/configure router ospf area 0.0.0.0 interface core_Test3 interface-type point-to-point
/configure router ospf area 0.0.0.0 interface core_Test3 metric 100
/configure router ospf area 0.0.0.0 interface core_Test3 authentication-type message-digest
/configure router ospf area 0.0.0.0 interface core_Test3 message-digest-key 1 md5 core-interface-md5
/configure router ospf area 0.0.0.0 interface core_Test3 shutdown

```

**Example: Output to file**
```
$ python3 sros-to-flat.py sample-sros-2.conf > sample-sros-2.flat
$ cat sample-sros-2.flat

/configure system name "aln-pe01"
/configure system dns
/configure system rollback rollback-location "cf3:\rollback-file"
/configure system snmp
/configure system time sntp shutdown
/configure system time zone UTC
/configure system thresholds rmon
/configure system security user "admin" password "$2y$10$g.M.jQ6ShDMovkCkhmg9P.p2UJjYHzEQ8TRXCF4hqO2JenG8bAEPK"
/configure system security user "admin" access console
/configure system security user "admin" console member "administrative"
/configure system security ssh preserve-key
/configure system security no per-peer-queuing
/configure system security cpu-protection link-specific-rate max
/configure system security cpu-protection policy 254 create
/configure system security cpu-protection policy 255 create
/configure system security cpu-protection port-overall-rate 15000
/configure log
/configure system security
/configure qos
/configure card 1 card-type iom3-xp-b
/configure card 1 mda 1 mda-type m5-1gb-sfp-b
/configure card 1 mda 1 no shutdown
/configure card 1 no shutdown
/configure port 1/1/1 ethernet encap-type dot1q
/configure port 1/1/1 ethernet mtu 1518
/configure port 1/1/1 ethernet lldp dest-mac nearest-bridge admin-status tx-rx
/configure port 1/1/1 ethernet lldp dest-mac nearest-bridge tx-tlvs port-desc sys-name sys-desc sys-cap
/configure port 1/1/1 ethernet lldp dest-mac nearest-bridge tx-mgmt-address system
/configure port 1/1/1 no shutdown
/configure port 1/1/2 ethernet encap-type dot1q
/configure port 1/1/2 ethernet mtu 1518
/configure port 1/1/2 ethernet lldp dest-mac nearest-bridge admin-status tx-rx
/configure port 1/1/2 ethernet lldp dest-mac nearest-bridge tx-tlvs port-desc sys-name sys-desc sys-cap
/configure port 1/1/2 ethernet lldp dest-mac nearest-bridge tx-mgmt-address system
/configure port 1/1/2 no shutdown
/configure port 1/1/3 ethernet encap-type dot1q
/configure port 1/1/3 ethernet mtu 1518
/configure port 1/1/3 ethernet lldp dest-mac nearest-bridge admin-status tx-rx
/configure port 1/1/3 ethernet lldp dest-mac nearest-bridge tx-tlvs port-desc sys-name sys-desc sys-cap
/configure port 1/1/3 ethernet lldp dest-mac nearest-bridge tx-mgmt-address system
/configure port 1/1/3 no shutdown
/configure port 1/1/4 ethernet encap-type dot1q
/configure port 1/1/4 ethernet mtu 1518
/configure port 1/1/4 ethernet lldp dest-mac nearest-bridge admin-status tx-rx
/configure port 1/1/4 ethernet lldp dest-mac nearest-bridge tx-tlvs port-desc sys-name sys-desc sys-cap
/configure port 1/1/4 ethernet lldp dest-mac nearest-bridge tx-mgmt-address system
/configure port 1/1/4 no shutdown
/configure port 1/1/5 ethernet encap-type dot1q
/configure port 1/1/5 ethernet mtu 1518
/configure port 1/1/5 ethernet lldp dest-mac nearest-bridge admin-status tx-rx
/configure port 1/1/5 ethernet lldp dest-mac nearest-bridge tx-tlvs port-desc sys-name sys-desc sys-cap
/configure port 1/1/5 ethernet lldp dest-mac nearest-bridge tx-mgmt-address system
/configure port 1/1/5 no shutdown
/configure system sync-if-timing begin
/configure system sync-if-timing commit
/configure router management
/configure router interface "system" no shutdown
/configure service customer 1 create description "Default customer"
/configure router
```
