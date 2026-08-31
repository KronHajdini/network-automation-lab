# Low-Level Design (LLD): FortiGate Active-Passive HA Cluster

## 1. High Availability (HA) Cluster Overview
This Low-Level Design (LLD) specifies the operational architecture for a high-availability perimeter firewall deployment utilizing FortiGate Clustering Protocol (FGCP) alongside a core layer configured with Cisco StackWise Virtual technology.

## 2. Cluster Specifications
* **Mode:** Active-Passive (FGCP Protocol)
* **Device Models:** 2x FortiGate 100F (FortiOS 7.4.x)
* **Heartbeat Links:** `port5` and `port6` (Directly connected, redundant)
* **Failover Time:** `< 1.2 seconds` seamless session failover via session synchronization.

## 3. Heartbeat & Sync CLI Configuration
```text
config system ha
    set group-name "EDGE-FW-CLUSTER"
    set mode a-p
    set password "ClusterSyncPass123!"
    set hbdev "port5" 100 "port6" 50
    set override disable
    set priority 200 # Set to 100 on Primary-02 (Backup)
end
