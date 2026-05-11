## Table of contents

<!-- toc:start -->
- [Purpose](#purpose)
- [Components](#components)
- [Requirements](#requirements)
  - [Lineage](#lineage)
  - [Auditability](#auditability)
  - [Self service environment](#self-service-environment)
<!-- toc:end -->

# Purpose

A data solution is a very generic high level concept that defines the total architecture that allows you to turn raw data into valuable insights. 

# Components
- Data logistics: the transport of data from source systems into a consolidated location where it can be used for analytics and reporting.
- Data modelling: Transforming the structure of data, or in other words the data schema. 
- Data cleaning and enriching: Transforming data, so that data quality improves.
- Data provisioning: Make data available for consumption by end users. 

# Requirements

A data element is the smallest part of a data object. E.g. a column value of a specific row in a table. 

## Lineage
It should be possible to show how every data element is constructed, by showing all transformations and logistic processes that are applied on top of the raw source data. 

## Auditability
Every read and write of a data element should be logged together with the related user, process and timestamp, so that it's purpose and authority can be verified. 

## Self service environment

**Synonym:** Sandbox environment
An environment that is less strict and hereby allows you to quickly load and use data. This can be used for ad hoc analysis of a new dataset or for research and development. Because of the lower requirements, this environment cannot be used for non R&D use cases. 