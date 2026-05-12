# Prompts

This document contains all the prompts used to generate and refine the content in this project.

## Session 1

1. I have renamed the Github repository to Data Engineering Design Patterns. Could you update my solution?

2. My solution contains several projects. I want to publish the Data Engineering Design Patterns project to a GitHub repo.

3. Check the naming of my repo and my files, whether they conform to best standards and practices.

4. Let's create a subfolder called definitions and create a markdown file for business intelligence and data engineering, and move the contents from the readme to these files.

5. Integrate the contents of the subfolder design pattern @DataEngineeringWithAI/readme.md  with the root folder @DataEngineeringWithAI/readme.md

6. Create a table of contents for the entire project, containing at the root level the README and, one level lower, the design patterns and definitions and all the markdown files in there. Add this to the end of each markdown file.

7. Complement this Markdown file with all the applications of Business Intelligence.

8. Summarize the applications in more generic descriptions and also change mermaid

9. Refer to the business intelligence node in the diagram to insights, and also change the applications paragraph to contain only the generic items reporting, analytics, and monitoring.

10. Rename Insights into Data Engineering.

11. Use consistent naming using snake_case (lower_case).

12. apply md naming conventions

13. Make sure that each markdown filestarts with a table of contents. This table of contents should not include the title or the table of contents reference.

14. Change motivation paragraph header in all markdown files to benefits.

15. Create a @DataEngineeringWithAI/readme.md  that explains the three documents.

16. Make sure that you use the naming convention. For example, event-based-orchestration should be separated by a dash.

## Session 2

1. do not include the tittle in the toc

2. do this when generating toc everywhere

## Session 3

1. This mermaid is not readable because it's getting too small. Can you generalize this mermaid ?

## Session 4

1. Add day to prompts markdown and sort by day.

2. Remove the session caption from each group in the prompts markdown, sorted descending so the newest prompts are at the top. Why are my latest prompts not present?

3. Sort the prompts markdown by the timestamp descending.

## Session 5

1. Include snowflake in the tool choice.

## Session 6

1. Create a plan for implementing a sample implementation using data engineering design patterns, based on free data ( e.g. OData). How can we trigger a refresh of this data for example?

2. ELABORATE THIS PLAN USING CBS (Dutch Statistics), Change-Detection Trigger (smarter) AND MAKE USE of Kafka and Apache Airflow

3. create a phase one implementation plan that is scoped on extracting the data from OData using event-based orchestration. Make sure that there is a strict separation between configuration and generic code. For example, the events and scheduling and triggering should all be configured using meta data.

4. change plan to reuse existing PostgreSQL and airflow on basnas. simplify roll out in steps.

5. move phase-one-cbs-odata-extraction to DataEngineeringIn2026 folder. rename to plan1

## Session 7

1. Create a new project called C2H-sales.

## Session 8

1. Explain to me how Apache Airflow can implement the event-based orchestration design pattern.

## Session 9

1. Defineer een naamgeving standaard voor het schrijven van markdown files (kebab case) en folders zodat cursor deze altijd gebrukt in dit project

2. Rename this file to match the title.

3. When choosing Apache Airflow, what's the most recommended setup? What other tools or frameworks are most often used?

4. Could you design an architecture for implementing event-based orchestration and create a markdown file for this under implementation event-based orchestration?

5. Doe maar een Azure-variant.

## Session 10

1. Create a sample implementation of the event-based orchestration design pattern based on Free OData Data from  the dutch government using Apache Airflow and Kafka. Make sure that the data is automtically fetched daily only when changed. Use PostgressSQL to implement the Object-Property tree design pattern to store all configuration. Keep strict separation of code versus configuration. Try to make the implementation as simple as possible. Start by creating a document called plan2.md. Create rollout plan in steps.

2. create a plan 3 based on plan  2 but replace the object property tree with a json following this schema https://github.com/data-solution-automation-engine/data-warehouse-automation-metadata-schema/blob/main/GenericInterface/interfaceDataWarehouseAutomationMetadataV2_0.json

## Session 11

1. The description for Object property tree in the readme in the root of the sign patterns is wrong.

2. Make sure that all the sign patterns have a table of contents.

3. What are the best platforms to implement event-based orchestration design pattern?

4. Could you create a subfolder in the design patterns called implementation? In this subfolder, create a subfolder for event-based orchestration. In here, create a markdown document that lists the tool choices as specified above. Also include costs and create an easy-to-understand fix on top of the document.

5. Rename this readme into toolchoice.md. Change quick recommendation paragraph into a comparison matrix.

6. So could you also add the option to let Cursor generate all the logic in a programming language like Python?

7. Please find all the relevant properties for a data warehouse orchestration tool or synonyms like ETL engine. One of the functionalities that is not listed currently is that it should connect, so it should support network functionality, for example:
- private endpoints
- credentials
- protocols

8. Refactor the current document. The goal of the document is to define the tool choice for selecting a data warehouse orchestration tool or ETL tool, or all the synonyms. Start by listing the functionalities at the top level, and then create a big matrix with all the tools and score all the functionalities with minus minus for very low and plus plus for very good.

9. Add costs to the comparison matrix and also whether it's open source or not.

10. Move costs and open source to the bottom of the matrix. Change costs to also use ++ and --.

11. Change cost indicator to use euro signs.Change 0 into +/min.

12. Why is Python + Cursor having three $ or € signs for cost, and why is Snowflake or Informatica not part of the list?

13. Yes, add all those tools to the list and split up the costs into engineering costs and infrastructure plus license costs.

14. Change cursor + python into self-built elaborate on this option by specifying the recommended libraries and languages to use for setting up an orchestration tool from scratch.

15. Add a recommendation at the bottom.

## Session 12

1. Explain this schema:
https://github.com/data-solution-automation-engine/data-warehouse-automation-metadata-schema/blob/main/GenericInterface/interfaceDataWarehouseAutomationMetadataV2_0.json  
The related doc is here:https://github.com/data-solution-automation-engine/data-warehouse-automation-metadata-schema/blob/main/docs/overview/Index.md 
My question is: why does it say "required": [
    "dataObjectMappings"
  ],
while the documentation speaks about dataObject ? 

does this json follow the schema? Does it validate?
@DataEngineeringIn2026/sample.json

2. Create a schema for @DataEngineeringIn2026/sample.json

3. yes for both. also create a Markdown file for follow-up tasks like specifying data types, classifications, and extensions.

4. How can I view the history of @DataEngineeringIn2026/sample.json ?

## Session 13

1. validate @data-engineering-design-patterns/implementation/full-data-solution/DataObjects/000_Source/dbo/CUSTOMER_OFFER.json against @data-engineering-design-patterns/implementation/full-data-solution/DataObjects/data-objects.schema.json

2. Update the schema to a single Data Object per file.
