'''
Title: 627. Swap Salary (Easy) https://leetcode.com/problems/swap-salary/

Runtime: 137 ms, faster than 89.67% of MySQL online submissions for Swap Salary.
Memory Usage: N/A

Description:
        Given a table salary, such as the one below, that has m=male and f=female values. 
        Swap all f and m values (i.e., change all f values to m and vice versa) 
        with a single update statement and no intermediate temp table.

        Note that you must write a single update statement, DO NOT write any select statement for this problem.

Example:
    | id | name | sex | salary |
    |----|------|-----|--------|
    | 1  | A    | m   | 2500   |
    | 2  | B    | f   | 1500   |
    | 3  | C    | m   | 5500   |
    | 4  | D    | f   | 500    |
    After running your update statement, the above salary table should have the following rows:
    | id | name | sex | salary |
    |----|------|-----|--------|
    | 1  | A    | f   | 2500   |
    | 2  | B    | m   | 1500   |
    | 3  | C    | f   | 5500   |
    | 4  | D    | m   | 500    |
'''

# Write your MySQL query statement below
update salary
set sex = CASE sex
    when 'm' Then 'f'
    ELSE 'm'
    END