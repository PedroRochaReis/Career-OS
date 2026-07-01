## Overview

Mottu was a technology-enabled scale-up focused on motorcycle rental, financing and the operational infrastructure required to move motorcycles from factory to branch. The role combined operational ownership of end-to-end motorcycle expedition and licensing with the design and development of internal systems that transformed manual logistics into automated, documented, scalable processes.

---

## Business Context

- Company: Mottu
- Industry: Transportation logistics, vehicle financing, motorcycle fleet operations
- Product: Primary product was motorcycle rental and financing; company also offered financial products
- Customers: Internal operations teams, factory planners, branch operations, third-party transporters, third-party licensing agents, regulatory and dispatch stakeholders
- Business model: revenue from motorcycle rental/financing and supporting logistics services across a large-scale motorcycle manufacturing and distribution operation
- Regulatory context: licensing and registration of zero-kilometer motorcycles; coordination with transporters, despachantes, municipal or state license plate production and regulatory requirements for vehicle movement
- Operational context: moving newly manufactured motorcycles from Manaus factory by river to Belém for registration and then by road transport to branch destinations; operation scaled to about 100,000 motorcycles per year, with 80 motorcycles per truck load and significant dependence on river conditions for timely deliveries

---

## Team

- Squad composition: effectively a one-person team responsible for logistics and expedition from factory to branch
- Reporting structure: not explicitly defined in raw material, but position was a Trainee with full ownership of the expedition and logistics area
- Cross-functional partners:
  - Factory production team
  - Planning team
  - Third-party transport companies
  - Third-party despachantes (licensing agents)
  - Branch operational teams
  - Internal operations stakeholders
  - Developers and technology partners later engaged
  - External suppliers for license plate production and transport services

---

## Responsibilities

I owned the operational and technical management of the motorcycle expedition and logistics area end-to-end. My responsibilities included:

- Managing the full transport and licensing flow for zero-kilometer motorcycles from factory in Manaus through river transport to Belém and onward by truck to destination branches
- Maintaining communications with factory, planning, third-party transporters, third-party despachantes, license plate producers, and branch operations
- Providing and coordinating all documentation required by transportadora and regulatory/licensing partners
- Aligning production, transport, licensure and billing processes across multiple teams
- Managing payments for the logistics area and tracking financial commitments
- Building automation and systems from scratch using Python and C#, including APIs to manage the area
- Performing analytical management: dashboards, bottleneck analysis, financial and risk analysis of the operation, and testing the systems under construction
- Executing operational work directly when required, including the creation of control systems and processes
- Improving traceability, reducing manual work, and moving the area from a person-dependent process to documented, automated systems
- Creating analytical tools that matched planning, fiscal invoicing, and real expedition status at the lot and motorcycle level

---

## Product Portfolio

### Product: Sistema de Expedição de Motocicletas

- Purpose: internal management system for the motorcycle expedition process
- Users: planning team, factory team, third-party transporters, despachantes, branch operations
- Business impact: reduced manual work, improved traceability, enabled scale, centralized operational control and validations
- Technical characteristics: C#, .NET, PostgreSQL, SQL, REST APIs, internal workflow and business rule enforcement, integration with external operational teams
- Stakeholders: operations, technology team, planning, factory, third-party transporters, despachantes, branch operations
- Dependencies: existing transport processes, factory production schedules, fiscal invoicing and shipment data, license plate production and regulatory approvals
- KPIs: SLA compliance for on-time motorcycle deliveries, reduction in manual cycle time, error reduction in shipment validation

### Product: Plataforma de Licenciamento de Motocicletas

- Purpose: platform to track and automate the motorcycle licensing lifecycle
- Users: internal operations, licensing agents, branch operations, transport teams
- Business impact: automated licensing steps, centralized information, reduced risk of delays and lack of responsibility, increased visibility into status of plates and payments
- Technical characteristics: C#, .NET, SQL, PostgreSQL, internal tracking system for license status, workflow automation for licensing stages
- Stakeholders: operations, technology team, internal stakeholders, external licensing service providers
- Dependencies: current licensing process, license plate suppliers, third-party despachantes, transport and branch handoffs
- KPIs: timeliness of licensing stages, reduction in manual follow-up, compliance with regulatory requirements

---

## Major Initiatives

### Name: Sistema de Expedição de Motocicletas

#### Context

The motorcycle expedition process at Mottu was highly manual and fragmented. The company produced around 100,000 motorcycles per year, assembled in Manaus, transported by river to Belém for registration, and then moved by truck to destination branches. The area was previously managed by a single operator with little documentation, no automation, and no system support.

#### Problem

- The process required constant manual effort and coordination across multiple teams and third parties
- There was low traceability and high retrabalho
- The operation could not scale reliably as production increased
- Critical shipment validations were done mentally or in disparate spreadsheets
- There was zero documentation of the process

#### Constraints

- The operation had to integrate with factory production, planning, fiscal invoicing, transporters, licensing agents and branch teams
- The solution needed to work in a high-volume environment with 80 motorcycles per truck and 100k motorcycles per year
- The area was the only person responsible for all work, so development and operational execution had to happen in parallel
- Climate and river conditions introduced variability in delivery timeliness and risk

#### Alternatives considered

- Continue using manual controls and spreadsheet-based management
- Build a solution internally to centralize and automate the process

#### Solution

- Developed an internal expedition system that centralized business rules, operational tracking and integrations
- Built validation logic for tripla validation: planning vs fiscal invoicing vs real expedition status
- Automated the end-to-end workflow from factory to branch, including documentation and transport coordination
- Implemented APIs and system components in C# and .NET with PostgreSQL
- Created dashboards and analytical tools for monitoring bottlenecks and operational status

#### My role

- Conducted requirement gathering with users
- Led product discovery and identified new boundaries for the system
- Modeled business rules and process workflows
- Developed backend systems and APIs
- Designed database models and handled data modeling
- Tested and homologated the system
- Managed implementation and rollout
- Owned the initiative as the primary contributor

#### Technologies

- C#
- .NET
- PostgreSQL
- SQL
- APIs REST
- Git
- N8N
- Python
- Power BI

#### Stakeholders

- Operations team
- Technology team
- Planning team
- Factory team
- Third-party transporters
- Third-party despachantes
- Branch operational teams

#### Decisions made

- Centralized the expedition process in a single internal system
- Prioritized critical operational functionality and automation before adding more advanced features
- Modeled the business process in detail before development
- Structured business rules modularly to reflect real operational workflows

#### Risks

- Building an internal system could take longer than continuing with manual controls
- The solution had to accommodate frequent process changes and diverse stakeholder needs
- There was risk of incorrect validation if planning, fiscal and expedition data were not integrated properly

#### Trade-offs

- Accepting initial development effort in exchange for scalable, documented processes
- Focusing on operational reliability and traceability rather than immediate feature richness
- Keeping the solution internal rather than using off-the-shelf tools

#### Metrics

- SLA compliance improved from approximately 65% per month to above 90% per month depending on Amazon river conditions
- Supported an operation of roughly 100,000 motorcycles per year
- Reduced manual operational work and improved traceability
- Enabled a cost analysis capability per motorcycle by integrating cost tracking from third-party transporters

#### Outcome

- A solid, responsible system that supported the motorcycle expedition process
- Greater visibility into operations
- Reduced operational errors
- Centralized information previously distributed across spreadsheets and manual controls
- Faster execution of expedition and licensing processes

#### Lessons Learned

- A good system must reflect the business process accurately, not just solve a technical problem
- Mapping the full operational flow before development is critical to avoid gaps
- Incremental development with continuous validation from users increases success
- Automating repetitive activities first creates space for more sophisticated product functionality

---

### Name: Plataforma de Licenciamento de Motocicletas

#### Context

The motorcycle licensing process involved multiple manual stages and stakeholders, with low visibility into the status of vehicles, plates and payments. The control was distributed and dependent on manual follow-up.

#### Problem

- Licensing workflow was manual and difficult to track
- Risk of delays and lack of clear ownership increased
- There was no centralized view of licensing status for each motorcycle

#### Constraints

- The platform had to integrate with existing expedition processes
- It needed to support license production, payment management, and alignment with transport and branch operations
- The solution had to work within a small team environment and parallel operational duties

#### Alternatives considered

- Retain the manual licensing workflow
- Build a dedicated platform for licensing lifecycle tracking

#### Solution

- Developed a licensing tracking platform that automated operational steps and centralized information
- Defined requirements with business areas
- Built the system using C#, .NET, SQL and PostgreSQL
- Integrated the platform with existing operational processes

#### My role

- Discovered the problem with business stakeholders
- Defined product and system requirements
- Developed the licensing management system
- Integrated the new platform with current processes
- Monitored the rollout and adoption

#### Technologies

- C#
- .NET
- SQL
- PostgreSQL

#### Stakeholders

- Operations team
- Technology team
- Internal stakeholders
- External licensing partners

#### Decisions made

- Choose internal platform development to centralize licensing
- Automate licensing status and workflow rather than keep manual tracking
- Align licensing visibility with transport and expedition operations

#### Risks

- The platform could fail to capture the real licensing status without strong integration
- External dependencies on license plate suppliers and despachantes could create delays
- Building a new platform while operating the area could stretch capacity

#### Trade-offs

- Built an internal tracking solution instead of continuing manual documents
- Prioritized operational transparency over rapid feature expansion

#### Metrics

- Increased control over the licensing cycle
- Reduced retrabalho and manual follow-up
- Standardized the licensing process

#### Outcome

- Improved operational control
- Reduced manual workload
- Increased standardization and visibility
- Created a foundation for future operational products

#### Lessons Learned

- Centralized tracking and automation reduce risk in complex regulatory processes
- Collaboration with business stakeholders is essential for licensing solutions
- A small team can deliver high-impact operational platforms if the scope is focused

---

## Technical Decisions

### Decision: Build internal systems instead of managing with spreadsheets

- Why: The process was highly manual, dependent on a single person, undocumented and not scalable
- Alternatives: continue with manual operations and spreadsheet controls
- Consequences: invested in development effort, created durable systems that scaled with business volume and reduced dependency on individuals

### Decision: Centralize the expedition process in one dedicated system

- Why: fragmentation caused retrabalho and a lack of traceability
- Alternatives: multiple loosely connected tools or continuing with ad hoc coordination
- Consequences: improved operational visibility, created a single source of truth for motorcycle expedition status

### Decision: Prioritize automation of operational tasks before adding sophisticated features

- Why: immediate value came from eliminating repetitive manual activities and reducing dependency on manual work
- Alternatives: develop advanced product features first
- Consequences: freed time for more strategic work, reduced operational risk, built trust in the new system

### Decision: Model business rules thoroughly before development

- Why: the operation had many interdependent rules across planning, fiscal, transport and licensing
- Alternatives: code before fully understanding the process
- Consequences: resulted in a system that matched real world workflows and reduced rework

### Decision: Use C#, .NET, PostgreSQL, REST APIs and Python for automation

- Why: these technologies supported backend development, integration, and analytical tooling
- Alternatives: other technology stacks or low-code tools
- Consequences: enabled robust internal systems, allowed direct control over development, and supported integration with analytics and automations

---

## Product Decisions

### Decision: Develop dedicated internal products for expedition and licensing

- Context: the operation had no system support and depended on human memory
- Reasoning: dedicated systems would provide documentation, traceability, and scalability
- Trade-offs: needed development effort and internal ownership rather than relying on external tools

### Decision: Centralize rules and validations in the system

- Context: disparate operational data sources created risk
- Reasoning: centralizing validations reduced errors and ensured consistency
- Trade-offs: more upfront work to integrate multiple data sources and stakeholder requirements

### Decision: Structure the solution around business rules and modular processes

- Context: the operation was complex with frequent changes
- Reasoning: modular rules allowed the system to adapt without major rewrites
- Trade-offs: required deeper initial analysis and design

### Decision: Use analytics and dashboards as part of the product

- Context: operational effectiveness depended on monitoring SLAs, delays, and costs
- Reasoning: dashboards would enable proactive management and decision-making
- Trade-offs: required additional development and analytics effort beyond core workflow automation

---

## Leadership

- Led the expedition project as the main responsible person, including initial discovery, development, testing and implementation
- Provided technical leadership by coding systems, defining business rules, and managing analytic solutions
- Influenced multiple areas: planning, factory, transport suppliers, despachantes and branch operations
- Coordinated external suppliers in licensing and transport services
- Created and organized the expedition process from end to end
- Led project execution and, later, worked with one developer while continuing to own the product and technical direction
- Exercised stakeholder management across internal teams and third-party partners

---

## Operations

- Owned the operational delivery of motorcycle shipments and licensing
- Managed KPIs such as SLA compliance for motorcycle deliveries and licensing timeliness
- Built dashboards to monitor SLAs, delays, river conditions, cost per motorcycle and operational bottlenecks
- Implemented monitoring of process performance and traceability across planning, fiscal invoicing and expedition execution
- Managed payment tracking for the logistics area
- Improved incident response by centralizing operational data and reducing manual dependency
- Turned an unstructured, manual process into a monitored operational workflow

---

## Metrics

- SLA compliance for timely motorcycle delivery improved from ~65% per month to above 90% per month depending on Amazon river conditions
- Motorcycle production and expedition volume: about 100,000 motorcycles per year
- Truck capacity: 80 motorcycles per truck load
- Estimated annual cost savings from transferring invoicing from São Paulo to Paraná: approximately 20 million BRL
- Visibility metrics created: cost per motorcycle, delay tracking by river condition, licensing lifecycle status
- Operational metrics: reduction of manual work, standardization of internal flows, error reduction, increased execution speed

---

## Technologies

### Programming Languages

- Python
- C#
- SQL
- Java (project Petrobras)
- JavaScript (basic, when necessary)

### Frameworks

- .NET
- ASP.NET Core
- Entity Framework

### Cloud

- Google Cloud Platform (GCP)

### Databases

- PostgreSQL
- SQL Server
- BigQuery

### Messaging / Integration

- RabbitMQ
- REST APIs
- Webhooks

### Architecture

- APIs REST
- Microsserviços
- Arquitetura Orientada a Eventos
- Event-Driven Design
- Integração entre Sistemas

### AI

- Gemini API
- Agentes de IA
- LLM Applications
- Prompt Engineering

### Analytics

- Power BI
- BigQuery

### DevOps / Automation

- Git
- GitHub
- Postman
- N8N
- RPA
- Web Crawlers

### Product / Project Management

- Pipefy
- Jira
- Figma (interface review/validation)
- Miro

---

## Skills Demonstrated

### Technical Skills

- Backend development with C# and .NET
- API design and integration
- Database modeling and SQL
- Automation with Python and N8N
- System architecture for operational processes
- Analytical dashboard creation with Power BI
- Event-driven design and integration
- Test planning and system validation

### Product Skills

- Product discovery and requirements gathering
- Business rule modeling
- Product definition for internal operational systems
- Prioritization of automation and operational workflows
- Product rollout and implementation
- Building products for internal stakeholders and regulated workflows

### Leadership Skills

- Technical leadership
- Initiative ownership
- Stakeholder influence
- Cross-functional coordination
- Supplier management
- Process creation and organizational change

### Business Skills

- Operational process optimization
- Cost analysis and risk evaluation
- Financial tracking for logistics
- Regulatory process understanding
- Business impact assessment

### Communication Skills

- Coordination with factory, planning, transport and licensing stakeholders
- Documentation of processes and system requirements
- Validation and feedback loops with users
- Presentation of operational status and risks

### Analytical Skills

- Bottleneck analysis
- Financial and risk analysis
- SLA analysis and monitoring
- Cost per motorcycle evaluation
- Data-driven decision making

---

## Stakeholders

### Internal

- Operations team
- Technology team
- Planning team
- Factory team
- Branch operations
- Product / process owners
- Internal stakeholders in logistics and legal/compliance areas

### External

- Third-party transport companies
- Third-party despachantes (licensing agents)
- License plate producers
- External suppliers for licensing and transport
- Potential external governance partners through regulatory compliance

### Customers

- Internal operations and process users
- Planning and factory personnel who depend on expedition data
- Branch teams receiving motorcycles

---

## Challenges

### Challenge: Manual expedition process and lack of documentation

- Problem: The expedition area was managed by a single person with no automation or documentation
- Why difficult: The process was high-volume, complex and subject to frequent changes
- Decision: Build a centralized system and automate the process
- Execution: Mapped the full flow, developed an internal system and validated continuously with users
- Outcome: Reduced manual effort, improved traceability, enabled scale
- Learning: Processes must be documented and automated before they can scale

### Challenge: Developing a complex expedition system with many stakeholders

- Problem: The system needed to integrate planning, fiscal invoicing, transport and licensing
- Why difficult: Many business rules, frequent process changes and disparate data sources
- Decision: Model the process thoroughly and build modular business rules
- Execution: Developed backend systems, APIs and dashboards, then rolled them out incrementally
- Outcome: A reliable system supporting the operation and reducing errors
- Learning: Deep process understanding before development reduces rework

### Challenge: Licensing process with manual status tracking

- Problem: Licensing lifecycle was fragmented and lacked ownership
- Why difficult: External dependencies and regulatory stages created risk
- Decision: Build a platform to centralize licensing tracking
- Execution: Defined requirements, developed the platform, integrated with operational workflows
- Outcome: Improved visibility, reduced retrabalho and standardized the process
- Learning: Centralized workflows are essential for regulated operational activities

---

## Mistakes

- The prior operating model relied on a single person’s knowledge and zero documentation, which was an operational failure point
- The absence of documented processes and automation created high dependence on manual coordination and increased risk across the logistics area

---

## Lessons Learned

- Building a system for business operations requires understanding business rules first, not just coding quickly
- Automating repetitive operational tasks is the highest leverage way to improve internal product operations
- Centralized systems create durable operational reliability where manual processes fail
- Technology solutions must be designed around stakeholder workflows and the real operational process
- A small team can deliver large impact by focusing on the highest-value process improvements
- Operational product work combines technical delivery, analytics, stakeholder coordination and ownership of business outcomes
- Risk and financial analyses can justify significant changes such as billing transfers and process redesign

---

## Keywords

Mottu, motorcycle expedition, logistics, expedição, licensing, licenciamento, regulatory workflow, transport logistics, factory to branch delivery, Manaus, Belém, trucking, river transport, SLA compliance, operational automation, business rule modeling, C#, .NET, PostgreSQL, REST APIs, Python, Power BI, N8N, internal systems, product discovery, process standardization, stakeholder management, third-party transport, despachantes, license plate production, financial analysis, risk analysis, dashboards, operational metrics, cost per motorcycle, event-driven design, integration, microsservices, APIs REST, architecture, analytics, product management, project management, Scrum, Kanban, OKRs, product delivery, data-driven product management, automations, test planning, monitoring, documentation, scalability, technical leadership, cross-functional collaboration, vendor coordination, supplier management