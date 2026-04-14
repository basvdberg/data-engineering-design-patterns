# Historic bitemporal table using recording time and valid time

When inserting data into a table, we record the timestamp that we make this change. This is the recording timestamp. We also record the time interval in which the record is valid. If this record, which is identified by a primary key, is changed, we don't change this record but insert a new record having a new record timestamp and potentially, but not necessarily, a new valid interval. 

Constraint: 
- A record identified by a primary key has no overlapping valid intervals. This means that when you record a change at timestamp `t`, the current valid record should be end-dated at `t`, and a new record should start at `t`.

When a new record is inserted, it has, by default, a valid interval that starts at the beginning of time and ends at the end of time.

Beginning of time (BOT) and end of time (EOT) are constants set to easy-to-read, very low and very high timestamp values (e.g. 1900-01-01 and 2099-01-01).

Reading from bitemporal table
1. Valid now view (default). This filters all records where the current timestamp is part of the valid interval.
2. Point in time view. This filters all records where a given timestamp is part of the valid interval.

#### Example

At `2026-01-01 09:00`, we insert:

| id | value | valid_from | valid_to | recorded_at |
| --- | --- | --- | --- | --- |
| 1 | A | 1900-01-01 | 2099-01-01 | 2026-01-01 09:00 |

#### Change handling

At `2026-02-01 10:00`, value changes from `A` to `B`.
We handle this by:
1. Closing the old interval at `2026-02-01 10:00`.
2. Inserting a new row starting at `2026-02-01 10:00`.

| id | value | valid_from | valid_to | recorded_at |
| --- | --- | --- | --- | --- |
| 1 | A | 1900-01-01 | 2026-02-01 10:00 | 2026-01-01 09:00 |
| 1 | B | 2026-02-01 10:00 | 2099-01-01 | 2026-02-01 10:00 |
