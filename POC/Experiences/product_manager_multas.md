# Product Manager — Traffic Fines Platform

> Company: Mottu  
> Role: Product Manager  
> Domain: Regulatory Operations, Platform Products, AI, Internal Systems

---

# Context

Mottu finances and rents motorcycles to thousands of customers across Brazil and Mexico.

Because every motorcycle remains legally registered under the company's ownership, all traffic violations are initially issued against Mottu rather than the rider.

The Traffic Fines domain was responsible for the complete lifecycle of every traffic ticket:

* Fine ingestion
* Driver identification
* Regulatory compliance
* Fine payment
* Customer charging
* Driver nomination
* Document validation
* Government integrations

Failures in these processes could generate direct financial losses of millions of reais every month, making the platform one of the company's most business-critical regulatory systems.

---

# Product Portfolio

## Fine Collection Platform

Responsible for automatically capturing traffic fines through integrations with SERPRO and government agencies.

Main responsibilities:

* Webhook integrations
* Event processing
* Customer identification
* Automatic charging
* Regulatory tracking

---

## Driver Nomination Platform

One of the most critical regulatory products inside the company.

Around 80–90% of traffic violations required Mottu to formally nominate the actual driver responsible for the infraction.

Failure to complete this process generated an additional penalty worth twice the original fine.

The platform handled:

* 35,000+ driver nominations every month
* More than 630 government authorities
* Multiple submission channels:

  * Government portals
  * Email
  * Physical mail

Monthly financial exposure exceeded **R$8–10 million**.

---

## NIC Product

Optional product allowing customers to avoid receiving driver's license penalty points.

Instead of transferring the penalty points, Mottu assumed the regulatory responsibility and charged customers an additional fee.

Business impact:

* Generated approximately **R$500k–1M monthly revenue**.

---

## Mexico Fines Platform

Owned the complete traffic fine operation in Mexico.

Responsibilities included:

* Fine collection
* Customer charging
* Fine payment

---

## Driver License Validation Platform

Responsible for validating customer driver's licenses before regulatory operations.

The platform processed both:

* Digital licenses
* Physical document images

Its main objective was fraud prevention and regulatory compliance.

---

# Team

Cross-functional squad composed of:

* Product Manager
* Tech Lead
* 3 Software Engineers
* Operations Specialist
* Intern

---

# Responsibilities

Owned the product strategy and execution for the Traffic Fines domain.

Responsibilities included:

* Product Discovery
* Product Strategy
* Roadmap prioritization
* Backlog management
* User Story writing
* Technical refinement
* KPI definition
* Operational dashboards
* P&L analysis
* OKRs
* Stakeholder management
* Operational management
* Business analysis
* MVP development using Python, N8N and low-code tools
* Software development for small business-rule improvements
* Product validation and experimentation

---

# Major Initiatives

## Operational Visibility

Designed new dashboards and operational KPIs.

Results:

* Weekly nomination completion increased from **94% to 99%**
* Two-week forward visibility increased to approximately **98.5%**
* Reduced monthly financial exposure by approximately **R$500k**
* Increased operational predictability

---

## Mexico Fine Recovery

Inherited a platform that had been non-functional for several months.

Within three weeks:

* Investigated root causes
* Designed a new collection strategy
* Built an MVP using Crawlers + N8N
* Restored the complete collection pipeline

Results:

* Recovered approximately **4 million MXN** in traffic fines during the first operational cycle.

---

## Mexico Payment Workflow

Designed a complete payment workflow integrating:

* Pipefy
* Operations
* Payment validation
* Invoice generation
* Internal systems

Replacing a fragmented manual process.

---

## Driver License Communication

Created an automated communication workflow encouraging customers to update invalid documentation.

Results:

* Digital licenses increased from **75% → 90%**
* Expired licenses reduced from **5.2% → 1.7%**

---

## Event-Driven Driver Nomination Platform

Co-designed a new event-driven architecture replacing the previous monolithic workflow.

Objectives:

* Improve observability
* Reduce operational intervention
* Increase scalability
* Simplify incident investigation

---

## AI-based Document Validation

Designed an automated document validation pipeline using multiple AI models.

Technologies:

* YOLO
* ESRGAN
* Flux

Results:

* 99% automatic validation for digital documents
* 90% reduction in operational workload
* Reduced manual validation from a full-time activity to approximately 20 minutes per day

---

## Customer Appeal Assistant

Created an automated workflow to assist customers with incorrectly issued fines.

The solution included:

* AI chatbot
* Appeal guidance
* GPS evidence
* Supporting documentation
* Government appeal instructions

---

## Microservices Migration

Led the migration of three critical systems:

* Driver Nomination
* Driver Documentation
* Mexico Fines

From a monolithic architecture to independent microservices.

---

# Most Challenging Project

## Event-Driven Driver Nomination Migration

This project involved migrating the company's highest-risk regulatory platform from a monolithic architecture to an event-driven microservices architecture.

The migration required extremely high reliability, as minor failures could result in financial losses reaching hundreds of thousands of reais.

Responsibilities included:

* Product ownership
* Business rule modeling
* Architecture definition (with Tech Lead)
* User Story creation
* Validation strategy
* Cross-system reconciliation
* Monitoring design

The resulting platform significantly improved:

* Observability
* Reliability
* Root cause identification
* Operational efficiency
* Incident response time
