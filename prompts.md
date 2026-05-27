# Prompts

This document contains the prompts used to generate and refine the content in **data-engineering-design-patterns**.

## Session 1

1. Do the same for data engineering design patterns.

## Session 2

1. is there a better word for data freshness @data-engineering-design-patterns/design-patterns/data-object-poller.md:38

## Session 3

1. I have renamed the Github repository to Data Engineering Design Patterns. Could you update my solution?

2. My solution contains several projects. I want to publish the Data Engineering Design Patterns project to a GitHub repo.

3. Let's create a subfolder called definitions and create a markdown file for business intelligence and data engineering, and move the contents from the readme to these files.

4. Integrate the contents of the subfolder design pattern @DataEngineeringWithAI/readme.md  with the root folder @DataEngineeringWithAI/readme.md

5. Create a table of contents for the entire project, containing at the root level the README and, one level lower, the design patterns and definitions and all the markdown files in there. Add this to the end of each markdown file.

6. Complement this Markdown file with all the applications of Business Intelligence.

7. Refer to the business intelligence node in the diagram to insights, and also change the applications paragraph to contain only the generic items reporting, analytics, and monitoring.

8. Create a @DataEngineeringWithAI/readme.md  that explains the three documents.

9. Make sure that you use the naming convention. For example, event-based-orchestration should be separated by a dash.

## Session 4

1. Include all the prompts like you did here @prompts.md also in the other projects.

2. @readme.md Update this readme with a disclaimer that explains that defining design patterns is a complex job that requires continuous refactoring and improving.

3. Related repositories should be at the top level of this project structure tree.Change the skill.

4. Create a new project called **cursor-config**.Move all scripts to this repo and all.git pre-commit hooks and all skills that exist in my user directory so that I have full versioning of this reference this repo where needed.

5. Check for other files that can be deleted. Also delete the.git hooks empty folders.

6. Update the prompts markdown in each project.

7. Review this linkedin post:
How is GenAI changing data engineering—not just coding faster, but how we design, document, and deliver?
I’ve started capturing that in an open repo: https://github.com/basvdberg/data-engineering-2026
The core idea: treat documentation and intent as fuel for GenAI, not paperwork you finish after go-live.

Documentation first — update design and decisions before implementation; AI drafts quickly, you review intent, then code follows.
CI/CD shifts — generated code replaces hand-written; docs become the specification that drives generation.
Specify what, not how — declarative standards (e.g. DSA metadata) and technology-agnostic design patterns reduce ambiguity so agents don’t wander.
The repo walks through this way of working (including diagrams on the old vs new data-engineering cycle), links to the Data Engineering Design Patterns collection, and points to a Data Solution 2026 proof of concept that puts the ideas into practice. This POC is in progress. I will report the lessons learned in the near future. 
#DataEngineering #GenAI #DataArchitecture #DataSolution #DesignPatterns #CodeSpecification

## Session 5

1. Create a new markdown file under Data Engineering Design Patterns, under the folder Design Patterns.

Replace this text in the current readme 'Calls separate what from how. Configuration vs code: anything source-specific (URL, paging, landing path, staging table) lives in DSA metadata extensions; the DAGs and the extractor stay protocol-generic.' With this reference to this design pattern, try to describe this design pattern similarly to the other design patterns.

2. Rewrite this configuration-vs-code design pattern. It should be named "Separate What and How", and it should be much more generic, not specifically for data solution but for any solution. It should describe that it's useful to separate functionality in a descriptive manner from implementation, which is imperative. This is because there is a one-to-many relationship between the two, because a specific functionality can be implemented in many ways.

## Session 6

1. Create a plan for implementing a sample implementation using data engineering design patterns, based on free data ( e.g. OData). How can we trigger a refresh of this data for example?

## Session 7

1. validate @data-engineering-design-patterns/implementation/full-data-solution/DataObjects/000_Source/dbo/CUSTOMER_OFFER.json against @data-engineering-design-patterns/implementation/full-data-solution/DataObjects/data-objects.schema.json

2. Create a @data-engineering-design-patterns/implementation/full-data-solution/dutch-odata-json/README.md  under the ADL folder that summarizes what ADL is using the following reference. Also include this reference:https://docs.agnosticdatalabs.com/docs/

3. remove @data-engineering-design-patterns/implementation/full-data-solution/dutch-odata-json and all references to this folder. move the things that you need to this new location. @data-engineering-design-patterns/implementation/full-data-solution/adl/Extractors

## Session 8

1. Check and rewrite Markdown.@data-engineering-design-patterns/design-patterns/data-object-poller.md

## Session 9

1. create a design pattern for a data object container using these markdowns.: @data-object.md @object-property-tree.md 
Use this Data Object Schema to enrich the data object design pattern. @open-meteo.json
