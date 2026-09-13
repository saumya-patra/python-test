import os

# Define the study guide content
content = """# Study Guide: Migrating AxiomSL to AWS Cloud (Financial Services)

This guide outlines key strategies, architecture designs, and high-probability interview concepts for migrating a data-heavy regulatory reporting platform (Axiom) from on-premises infrastructure to AWS.

## 1. Migration Architectural Blueprint

| Infrastructure Component | On-Premises Solution | Recommended AWS Target State | Justification |
| :--- | :--- | :--- | :--- |
| **Application Nodes** | Fixed-size Unix/Linux bare-metal servers or VMs | **Amazon EC2 (C6i / R6i families)** within an **Auto Scaling Group (ASG)** | Handles intense compute peaks during month-end reporting; scales down during off-peak days to optimize costs. |
| **Database Engines** | Oracle Exadata / MS SQL Server Clusters | **Amazon RDS Custom for Oracle / SQL Server** | Retains OS-level administrative privileges needed for Axiom configuration while offloading backup/patching operations. |
| **Shared Storage** | Network Attached Storage (NAS / SAN) | **Amazon EFS (Elastic File System)** | Provides elastic, POSIX-compliant shared file storage for Axiom application objects and user profiles across multiple AZs. |
| **High Performance Disk** | Local SSD Arrays | **Amazon EBS (io2 Block Express)** | Meets the extreme IOPS and low-latency storage demands required for massive database processing queries. |
| **Data Ingestion** | Legacy SFTP Servers | **AWS Transfer Family (SFTP)** integrated with **Amazon S3** | Automates financial source file ingestion securely. S3 serves as a landing zone capable of triggering automated processing. |

## 2. Security & Compliance Checklist (Banking Standards)
* **Data Encryption:** Enforce KMS-managed encryption at rest across all S3 buckets, EBS volumes, and RDS instances. Utilize TLS 1.3 for data in transit.
* **Network Isolation:** Isolate all application and database servers inside Private Subnets. Use AWS Direct Connect for secure, dedicated backhaul to on-premises data centers.
* **Identity Management:** Map AWS IAM roles to corporate active directories using AWS IAM Identity Center to support Least Privilege Access (LPA) principles.
* **Auditability:** Enable AWS CloudTrail, VPC Flow Logs, and AWS Config rules to monitor infrastructure changes and access patterns continuously.

## 3. Key Migration Process (Step-by-Step)
1. **Assessment:** Utilize tools like AWS Application Discovery Service to map system dependencies, upstream data feeds, and downstream consumers.
2. **Data Replication:** Use AWS Database Migration Service (DMS) for continuous Change Data Capture (CDC) replication from on-premise databases to RDS Custom.
3. **Infrastructure as Code (IaC):** Standardize environment provisioning across Dev, UAT, and Production using AWS CloudFormation or Terraform.
4. **Validation:** Execute automated parallel-run testing where identical data inputs are sent to both on-premise and AWS environments to verify that Axiom produces identical regulatory outputs.
5. **Cutover:** Execute a low-downtime cutover utilizing Amazon Route 53 to redirect network traffic to the cloud once the DMS replication lag drops to zero.

## 4. Key Performance Indicators (KPIs) to Track
* **Batch Processing Windows:** Ensure time-to-compute regulatory outputs is equal to or faster than on-premises.
* **IOPS & Throughput:** Monitor EBS volumes to prevent bottlenecks during heavy aggregation scripts.
* **Cost Efficiency:** Measure the ratio of idle infrastructure costs vs. active processing costs via AWS Cost Explorer.
"""

# Create directories
os.makedirs('generated', exist_ok=True)

# Write the file
file_path = 'generated/axiom_aws_migration_guide.md'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content.strip())

print(f"File successfully created at: {file_path}")
