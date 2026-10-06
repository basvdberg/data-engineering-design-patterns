The purpose of documentation:

Documentation is usually created for the following types of readers:

1. Other data engineers, team members, and future colleagues.
2. Data product owners.
3. End users, stakeholders, and analysts.
4. AI agents.

Each reader has a different purpose and requirement.

| Reader | Purpose |
| --- | --- |
| Data engineers | Maintain and extend the data object |
| Data product owner | Support functional maintenance and communicate with stakeholders |
| End users, stakeholders, analysts | Understand business definitions: how column values are constructed from source data, which filters are applied, which assumptions were made, and which business rules are implemented. This is needed when using this data object for a reporting or analytics task, for example to determine whether it is suitable for answering certain questions. |
| AI agents | Understand the purpose of this data object and how it should be populated from source data. Provide an unambiguous specification. |

Documentation should therefore explain both the business meaning and the technical implementation of the data object so that each reader can use it effectively for their purpose.
