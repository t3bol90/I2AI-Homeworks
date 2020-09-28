# **HOMEWORK** 01

Courses `CSC14003`: Intro to Artificial Intelligence
18CLC6, FIT - HCMUS.
`17/07/2020`

-   `18127231`: Đoàn Đình Toàn (GitHub: [@t3bol90](https://github.com/t3bol90))

---

## Problem 1. (2.0pts)
**Give a PEAS description for each of the following activities**

**a. A tailor is sewing clothes on the sewing machine.**
Assume that a tailor is a human agent, the PEAS description for this agent will be as follows:

- **Performance**: The Performance factor for a tailor will be the Correctness of sewing, Safety, Productivity, Time, etc.
- **Environment**: The Type of fabric, Style of clothes, Type of sewing machine, Place where this tailor work (at home, factory, ...), the Sequence of task (complete clothes or just a module),  ...
- **Actuators**: The actuators is the part do the action of tailor: Hands, Legs, and other body part.
- **Sensors**: All 4 senses of tailor (not Taste), but Sight and Touch are the most importance senses for sewing. The Tailor need to see where the needle of sewing machine, using their hand and leg to control the machine (touch to know), feeling the type of fabric, change the form of clothes for some anchors, symbols,... Sometimes tailor can Smell or Hear the broken signal of machine, some power issue (if the machine is electrical sewing machine). 

**b. A customer is ordering food on GrabFood by using his/her smartphone.**

Assume that our customer is a human agent, the PEAS description for this agent will be as follows:

- **Performance**: The Taste of food (good or bad), Prices, Feelings, Time, Experiences, etc.
- **Environment**: GrabFood application is an environment (it's fast, updated to newest version, outdated or not, supported or not,...), the Location of customer, Speed of the Internet, Type of his/her smartphone, etc.
- **Actuators**: Hands, Mind, maybe some part of body that can 'touch' to smartphone's screen.
- **Sensors**: Eyes, Ears (some restaurants have video as ads), Nose (in case our customer smell somethings and feel hungry :<), etc.

## Problem 2. (2.0pts)

**Examine the AI literature or the Internet to discover to what extent each of the**
**following tasks can currently be solved by computers/robots:**

**a. Real time translation of spoken languages, e.g., from English to French, by Google Translate**
**Extention:** Real time translation have been embed in many application and device (Skype Translator calling, Microsoft Translator, Google Translator - Google Assistant, WT2 Language Translator..). But it's performance sometimes does not good enough in some case and complex languages - hard accents because of some NLP's problem in that languages haven't solved yet, eg: Google Translate can not translate correctly 'con cua có càng lớn và càng bé' from Vietnamese to English.
**Rating:** 3.5/5
**References:**

- [Amazon]( https://www.amazon.com/Language-Translator-Portable-Translation-Shopping-Black/dp/B07GQZC7S7)
- [WT2](https://www.imore.com/best-language-translation-devices)
- [Voice interfaces for real-time translation of common tourist conversation](https://www.researchgate.net/publication/236954457_Voice_interfaces_for_real-time_translation_of_common_tourist_conversation)

**b. Fingerprint recognition in smart devices and laptops**
**Extention:** Fingerprint recognition was one of the first techniques used for automatically identifying people and today is still one of the most popular and effective biometric techniques.TouchID of Apple (use for app/security authentication), Thinkpad's fingerprint are good example of how far fingerprint recognition have been. It's fast, high reliability but also have some potential security risk.
**Rating:** 4.5/5
**References:**

- [Fingerprint Recognition, Overview](https://link.springer.com/referenceworkentry/10.1007%2F978-0-387-73003-5_47)
- [ngerprint Recognition](https://www.sciencedirect.com/topics/computer-science/fingerprint-recognition)

**c. The mastering of board games, including chess, Go and Shogi, by AlphaZero**
**Extention:** Alpha-Zero system learned to play three challenging games (chess, shogi, and Go) at the highest levels of play seen. It was train on TPUs via process of trial and error called reinforcement learning and the important thing that many professional of board games include chess, Go, and Shogi said that AlphaGo is creative. In chess, AlphaZero won in all matches at 2016 TCEC, winrate 91.2% in shogi and 61% in Go.

**Ratings:** 5/5.
**References:**
- [ AlphaZero: Shedding new light on chess, shogi, and Go ](https://deepmind.com/blog/article/alphazero-shedding-new-light-grand-games-chess-shogi-and-go)
- [Mastering board games](https://science.sciencemag.org/content/362/6419/1118.summary)
- [DeepMind’s AlphaZero beats state-of-the-art chess and shogi game engines](https://venturebeat.com/2018/12/06/google-deepmind-alphazero-chess-shogi-go/)

**d. Autonomous spaceport drone ship (ASDS) by SpaceX.**

**Extention:** Autonomous spaceport drone ship (ASDS) by SpaceX is an ocean-going vessel derived from a deck berge, outfitted with station-keeping engines and a large landing platform and is controlled by an autonomous robot. It's a innovative thinking from SpaceX when build ASDS allow SpaceX to land boosters at sea on high-velocity missions that cannot carry enough fuel to allow for a return-to-launch-site landing. It will be a opening door for safety space travel and exploring the universe.

**Ratings:** 4/5. - It's a beginning, but it work well after many times trying fail/success and testing.

**References:**
- [Wikipedia](https://en.wikipedia.org/wiki/Autonomous_spaceport_drone_ship)
- [Reddit](https://www.reddit.com/r/spacex/wiki/asds) - I do not want to put it here but it's good references to another paper/references for more detail.

**Write down your findings in 2–3 sentences each. The finding should rate the level of intelligence required on the task, on a scale of 1 (lowest) - 5 (highest), and then give explanation.**
## Problem 3. (3.0pts)

**Consider the following graph. The start and goal states are S and G, respectively.**

![](https://i.imgur.com/1HWSAVO.png)



**For each of the following graph search strategies, work out order in which states are expanded, as well as the path returned. In all cases, assume ties resolve in such a way that states with earlier alphabetical order are expanded first. Remember that in graph search, a state is expanded once.**

Define:
- (v, w) : notation for node v behind node u one step in the optimal path with weight = w. (weight depend on the algorithm)
- (v, w)*: expanding complete.
- x or 'null': not expanded.
- g: reach goal state.

**a. Depth-first search.**

Apply Depth-first search on the graph have this table bellow:

| Step | S          | A          | B          | C          | D          | G     |
| ---- | ---------- | ---------- | ---------- | ---------- | ---------- | ----- |
| 1    | **(S,0)*** | (S,1)      | (S,1)      | (S,1)      | x          | x     |
| 2    |            | **(S,1)*** | (A,2)      | (S,1)      | (A,2)      | x     |
| 3    |            |            | **(A,2)*** | (B,3)      | (A,2)      | x     |
| 4    |            |            |            | **(B,3)*** | (C,4)      | (C,4) |
| 5    |            |            |            |            | **(C,4)*** | (D,5) |
| 6    |            |            |            |            |            | **g** |

Expanding order: S, A, B, C, D, G.
Path: S -> A -> B -> C -> D -> G (cost = 19).

**b. Breadth-first search.**

Apply Breadth-first search on the graph have this table bellow:

| Step | S          | A          | B           | C           | D           | G               |
| ---- | ---------- | ---------- | ----------- | ----------- | ----------- | --------------- |
| 1    | **(S,0)*** | (S,1)      | (S,1)       | (S,1)       | x           | x               |
| 2    |            | **(S,1)*** | (S,1),(A,2) | (S,1)       | (A,2)       | x               |
| 3    |            |            | **(S,1)***  | (S,1),(B,2) | (A,2)       | x               |
| 4    |            |            |             | **(S,1)***  | (A,2),(C,2) | (C,2)           |
| 5    |            |            |             |             | **(A,2)***  | (C,2),(D,3)     |
| 6    |            |            |             |             |             | **g** as (C,2)* |

Expanding order: S, A, B, C, D, E.

Path: S -> C -> G (cost = 10).

**c. Uniform cost search.**
Apply Uniform cost search.

| Step | S          | A          | B          | C          | D          | G      |
| ---- | ---------- | ---------- | ---------- | ---------- | ---------- | ------ |
| 1    | **(S,0)*** | (S,5)      | (S,1)      | (S,6)      | x          | x      |
| 2    |            | (B,3)      | **(S,1)*** | (S,6)      | x          | x      |
| 3    |            | **(B,3)*** |            | (S,6)      | (A,7)      | x      |
| 4    |            |            |            | **(S,6)*** | (A,7)      | (C,10) |
| 5    |            |            |            |            | **(A,7)*** | (D,8)  |
| 6    |            |            |            |            |            | **g**  |

Expanding order: S, B, A, C, D, G.

Path: S -> B -> A -> D -> G, (cost = 8).

**d. Greedy search with the heuristic h shown on the graph.**

Apply Greedy search with h on graph.

| Step | S          | A     | B          | C          | D          | G              |
| ---- | ---------- | ----- | ---------- | ---------- | ---------- | -------------- |
| 1    | **(S,0)*** | (S,3) | (S,1)      | (S,2)      | x          | x              |
| 2    |            | (S,3) | **(S,1)*** | (S,2)      | x          | x              |
| 3    |            | (S,3) |            | **(S,2)*** | (C,2)      | (C,2)          |
| 4    |            | (S,3) |            |            | **(C,2)*** | (C,2)          |
| 5    |            | (S,3) |            |            |            | **g** as (C,2) |

Expanding order: S, B, C, D, G.

Path: S -> C -> G, (cost = 10).

**e. A\* search with the same heuristic.**

Apply A-star with f = h + g.

| Step | S          | A     | B          | C        | D          | G              |
| ---- | ---------- | ----- | ---------- | -------- | ---------- | -------------- |
| 1    | **(S,0)*** | (S,8) | (S,1)      | (S,8)    | x          | x              |
| 2    |            | (B,6) | **(S,2)*** | (S,8)    | x          | x              |
| 3    |            | **(B,6)*** |            | (S,8)      | (A,9) | x         |
| 4    |            |  |            | **(S,8)*** | (A,9) | (C,10) |
| 5  |            |  |            |          | **(A,9)*** | (D,8) |
|  | | | | | | **g** |

Expanding order: S, B, A, C, D, G.

Path: S -> B -> A -> D -> G (cost = 8).



## Problem 4. (3.0pts)

**You are given the initial state (a) and the goal state (b) of an 8-puzzle as shown
below:**
![](https://i.imgur.com/olLuiFJ.png)
**a. Apply A\* using Manhattan distance heuristic function. Draw the search tree including possible expanded states during the algorithm procedure. Compute the triple (g, h, f) for each state. Mark the optimal strategy found.**

![](https://i.imgur.com/xbjECxq.png)



Assume that we can go back to previous state when expanding. Sorry because small font size of `tkinter`.

For HD resolution: [drawio viewer](https://viewer.diagrams.net/?title=Untitled%20Diagram.drawio#R7L3X1qPG1jZ6NWuMvQ9WD5HhsMiSiBIS4YyMECCJDFf%2FV%2FG%2Bbbft9kq2O7i%2FttVdQkDBrDDnM%2BM%2FCKGelTZ8FvojSat%2F4Ltk%2Fgch%2FgPHCYrg4D%2FoyPJ2BKOo3duRvL0l78d%2BPnC%2Bren7wY%2BnDbck7X5xYv94VP3t%2BcuD8aNp0rj%2FxbGwbR%2FTL0%2FLHtUve32GefqbA%2Bc4rH571L0lffF2lMWZn4%2Br6S0vPvaM0e9vXIcfT35%2Fk64Ik8f0ySFC%2BgchtI9H%2F9aqZyGtEPU%2B0uXtOvl3fv3pwdq06f%2BTC%2FJao08nQhbHK4kzUXY7SsU%2Fibe7jGE1vL%2Fw%2B8P2y0cKwOd%2Bouat3kjFj2nb3yCBtDBKK%2BvR3frbo4G%2FR4%2B%2Bf9TwhAr9wIfxPW8fQ5MIj%2BrRbrcisu3PJ%2FcA1S1H1%2FaPJzwads%2B3Icxucwqfmt%2B6BB%2BP7j4ege0k7MN%2FEODtKy4%2Fm%2FwfuHC78uZp2h2V%2FAHgH%2BN8KaRLDlsB%2BkuuBODDf0XXgFfQZ3QKrxrC%2BWrvBZDvM1Dcb9vBane6FrsLztWJmhRxfQEBTo2Re%2Blj3FgC9zrEeDEmJiuOK4mueCXS1U8k9Ju8C11u2MunJzwfXIjrsBclai89sUgAiy7upz38mKUEP5dlL3STQSW46LPwNrl6vpz4q3qLmWRMnNR4KBJfpNQ1Dff68MzN%2Bnar7ud77vW8FMZAupAa4RfgXmSMECeukJ3mx4FfNVqrGAo%2F%2FAPnnTiyghXoINOO8K2rCj6vgY5PQLAlPgdSvhdt5YAxz4SA%2F41e33dGX92ABSnKrz3DR2IYVbTYwcuxiZJLG4y3IAoAuFvF2ScCQkEXLnBByHA2ySZzgX8zHvzLygV4j76%2F0qPHrOSDzayFhkfYlBmY3nXxjJmHBB5Iur7q1pFJOu8ixFrvjgTDpaN123GWMztpKuyiuTUj38wV0oMLaxDIB0Oohhr3TJb5IUhvHVwQ%2FLiqmAX%2FfRkYWiAyM%2BtBmvancwEG%2BCxynHmEr%2Fqw5RGjAM%2BUA2JmDyt9uoEWr2OKaNBbm7smmXegNZKWIHX%2BoUlhgd4f%2Fs%2B3xNh5U8bcQ74knhQ%2FWgyH3qnCWAlRdmxWChJ8gueKJPyulZ3d5hQ8R86IaRV80WeiNU7bAh6ZLHHitHZ%2FiQyJcM64oEzuOs3ryUDXWyvLDjPuihn80swknxvArgE4g1wHoOZho4CNOw%2FCjw0f8HAy73jhrQFH2ZdgQ3ob7sfHxvu4S4e3BgCH3IYNBzaArfzU2Lr6Cn02lmLuGdHcU5o2WfkZe%2FSjz0c6yZS6Dmmx7roxL4o5DQ65VQxq75mLX66sFDwgxRnZJpMBNvhJiveTCmDzELNF23c3vBHPIGN1ihJwHnf2vqrow7APSVWIJxZQJlw%2BYeSPgdqMmj7fyGlg7vszGeNP9iAvwijYc0webV7FTU3USVve0fPBCwOTuvXwyVxpNs2JMdDiuU3rao03A8tjHs4e%2FjIx81oU8Z6hTInL1xKwgEcjq9jf6Tj9l322lm896yoMCyI2NYs%2FuqF4YQOqGZJZPSQpvyavjrt3o%2B3kAvYasbclF0%2FO7QAsMfDaaK8WbAb3IQUSmy%2FhB9GP9PnW4l08FGMiWtn0Eaw6XFjzoSXtwNitNmutb6eqh85Iukmh0Cq3Csgw%2BRMIvh8K%2FrE%2BeV%2BLcOCuR5NkR4tdp3HgD8OSUbG4twISEohXY0YurZG06yM2q2CnRPMSCYwllOWdXOcoIPc2f1EBWlQyGHEZLjjZcUVc4W1zzawOzuVGTRF9cYBRjivgImjVFETi0Y1yvePyPp%2B0yYzPyh5YpnWZg4yeTk7kB%2FCaeNex0jMY9CVP7otymG9GWcrRYW5u0%2FI3GYX%2FsE%2B57NXd6vSGTQ%2BqXOeYpfOvVGfhnuJAtnimWTFXuPt4ZaJ9buZsdJC5sSQHEyyD5BEbvxH1Q24Q5T5qNDMqsczyeTJVn4EvrMmjfkWQBfFZQ1FJ0XWKjptKgrhOvfyAa0IwSU713vg%2FpJTQnkZ1d11BZZ9qk6fPF05FDJvt9cka%2FX05CtfzS13BmW1YEMeCVtwPNShnyTclIyZN%2FY0XOUIsNmwAxa%2ByYAeTE%2FgjWepybyrFvJq8VfNH6n1u891wbitl8KX2Fn8n1Puz%2BhSlcOTy%2BhVWWKcY%2BjzEfumTQbA2qUfRafWkVZtn90i8wtIxj565KPuL5gBpj%2BRvcL5czdOREvz9HiENgv8tOHrHSwh5pPMnh97BkpI%2B6rRvF3jK%2B684%2Bw7c3qEr%2Bf51%2BhkGwnM%2BUO9IsPgEBeK793PDd%2FSZ%2F3T3nwEabLxjtP8Cr5G%2FwWv7BgkeELCFPURCu%2F8PSh677Rf0DAJ6sI8H6LBGKKuJuudGoR35dkL20xXk%2F%2F8b9AeJBV%2BKL%2FoaPqeIwWbXt497%2BhHVNY8GgcLsVlW%2FOhS%2BY7sYDkHafgb01bckQd3wU3Hr0%2FMzjFGfUxuix9ugIwKBG%2BzLHk1%2Ffn%2BozwDf%2F35smZ8H7n14ceoz40vsPje4f9HYUj8GFr8jLH5%2Fx%2BLL6%2BIfvi4S32NmqWMbEicPNyDoCIlfPkHip8v5ECh78cTcsHVv40sNpp2Qm4Gkr4IhCrzYAYCDWONpKYoz2yFEvAlfD0k1H%2B9i52WTZPkyNGsWq82JB%2BSBg9hGQGLUQp%2FAmV9jlhzba9iia2K8ZnFPm0L0OxWubW3DI1h7taCUJLfdLIu%2BkM2EFIBDZZ1ciGIjOWyvCIRn6Rl7ZlmI8DiLrpcniDuBLk6s1S1vD4I2Uq8lnMRvr8FYImyLqxRHR3FVd2tDpbu%2B5VORHg2GHJm3l7CIdqbT5kk4MSn7xI3ooBQP8bhTv93Q8wLzKjK3Rhi8Ej3ly7A120y7dlW5FkkWZyTQE6WJZkmS3qqc31njRLBNl5UUsaMQYB%2Bjhhyt2M8PSLJv9byLsoMGsjriiHXUbfRCJXoiB5wF5xSHVwHOHQiSrZJkPRdEXqRhqcgauVEWNfxUUEKyCMqE04bgmPY6PcPgqTzprMHYrJ4wfAVhw5iRaJ3uQL8hjhe8NdBcRRxv3YNAQhwPNg7gpNhg2UOOd6q3hg74Go4fKPWcv58gx4MNyPHgyIj7G%2BR4yltjAkqAOJ6%2BAOWEuCxsQNb3tfosU8%2FrBEzpkhlXaKLCSOWK2%2FG8ptZqZ2IsTp4JiRyVRVzqLv9As6lFu5rVOORe30%2BrnknqeFRJZi8aOZNDWA738YhsdBBbvKpavGk7da2XwGOEIFYK4mSGD0YgiMAEYlIMEJjzj2wJWMGqxMDkdXgXKDYlVQxC3vebskuMeDmtvjoXKuL8S4TvVp3vxx7rObs5g4WfJjVmJ%2FlJ3azAZ7S%2F%2Faj91GcZr%2BKOchKDaEk9m%2BplmpVpopYc6dfkK52qCIGN3Skc1EOdL1f4cc1lEveqTBysTTHl1SDwNAtLy52ec01eG01eWVfa8jgLLhaca0dverrhc2gM3S8DX0%2B6WH8OVrF4EB%2F8zSj6e30K1JDZQttLZPliIW0jJosEmpZCZo%2B2VrTPNMVs8jFDDaYMp6Q%2Fc%2FIUK6dB66YjWkNBXqfmYjm%2BkW8q2HMe5cJa1M0SL%2Fo0aQUTRa3XLZr4YHlPerGPbK%2BKoFtV2Spu15oUHSIApK%2FshRE9UsOIO9kNUlNgIpJbkoMbigc3Ko2DRPli4aOh8svQNc%2Bk%2BP3Q%2BU%2Fpc6CedPwcagZjJct3Njr48XwOOO%2FBWSIaPw%2Ff955Yr9PpuE6BFhznGsQ05r6QSvHc4%2FKhUWc21rS90fYVPRa4NCnzGq1xNBIMOw6zMOx6IiGy5bqaRM946VicO8xJzMifhXXymYA8nJ71I2SGdcw0iM3%2FJtT9d33uS1MnS9MgafcaEzpeyQRvVHlwGzikm2d3L9Dgj%2FhEjIr6VAN9jX3rcQcUc8hU1YiTx8E66ALF8Nl6UkI%2Bt1UziDj%2FUMI5v4DpCXmLKOkiK3oxvB3IyKeuR4gvkYDdwzWjgisgVon06BnfmRL18NBLLfvGAld7nZQstPsZ7l22A3%2B7tH%2FTUfhsnwZhWE5v7QgInosVRJooRSt%2FJ2qWwMlULgbtXVCFYLu50Zw6CKobYi6UC4QrvuJoz%2FIOo0H1B43ct5yAV82qYV5smNEGwKVKdu7nwa4F4c9B378C3wT2OfTNfWDYL4m%2B6d8gtE%2FgNvbv4Dbxw8Jt5ueBeh9P6nPj%2BUXRNvNjoO0LQtvPN7TNXwTmGnxltI2b5WXa0PZ8uIT0Dt4GItaf0XYRJb2rSPyp60HHntp0X%2FTkbVouWrQo%2FR4oLBC7Enu9NFlZGpn2HHUyJV24IJl2s6eNwmb8uxlwOHkMV3KQs0Z2FiYxXxfpte2hvqC%2Ftj30AvTXXrCVYKWpzoIY2WvhRMR3XCQCNLF6qieOEHNwxe20o5EEsWCrBKyCMy1S2FuGdnGa%2BOJAcM2vCH2bJwbBXLrfUaxIWum66dhXinU1gtm08sikpaozmRLFojZXJkNGchJDT0vgFDJsRe4SA5rRKDa11NkfGCJlEpWZrreYI7nySDi56AaOrnM7746wEU0hs2j9SB87wCkIHlfI6JklTnk0WzxlOXq9w4fn99IkZAgbMNbrtGzm6tRp0HsyMSNTzPwCBBuTEFlc1BtODZNIDg0Ub31eV4srcbT5DL2dEiyjtbKkpvn7XarOyHLkOxB8i%2FvIs6zazghnxxlnGj4IN44ca2lL3E64Mi%2B%2B6DKzA1xQHjdedwXi8QYbynXjdQ%2BgXDde9%2FlxkuCEhrxOyOHMRrxueSBeJ28NyOtkyOseOWxUG389wjm98dfjxl%2B%2FTp%2BrEj35cDWQRduQME0j9asSZ1Cm9Cifzwc0GlqOwAWvvg4LadxOrOcZo96us8%2BXNYlLFjwdC446Un7kPbOInEQF18Lf0xTJ0wJ74065jQB46olDbDoVbXZZ82qAapNR8eInprHr0bzbsnfzSltDfcq5FhXg0jZqbCB5KlleowM89TKFNbXGRqdLuLOu8JEPV694SBT1OESrHlczxn7zNP%2FT%2BhTDBpmgRy57VViHsDQ%2B6vwrU8LgVRMuTXDiA%2FkXAJ1EJN3n8YoWfNqgUfUaELSGWqKdSZ9EJRTPeCiGHMleiApZNV5quOpZy2ZeRaVln9T5ZK7TGTfH6Tui0R%2FsMzoE6XR46SRRsunzVfPXTKifqzk7gi9GhXyVaYPEbyupa7F3yK%2BDzswYLjjg%2BPYccD42FoTKhHgy0JznyfL4goOhl7qU3MS90RxH%2FlS2XIqf39SHPXwmETkPKP0UdRQWbNqrU3WCZ9zIuV7RWacZWbiD74eOf0afNWdqCCQjLRImPn0zsngDeWmgGbyDXGHosZ5WbZEFH%2BlDqQ3LQV4wDmB1aciu4lOudKxUwQ8WUfTTEnecFl3Ma72ppCd21JAWWg0Zi8%2BTJpe7JPueaPTH%2BrTx88LlYhzMjYpx9QsB2PTsdoRzM%2BEOWyjmFGFwBkOcK2FTqLRsr8cm3fL42SRpNiAe2LLeV5Aly7PRZCrWKT3Wx6caTpR0csnzVSApb0L%2BLfvhMSpSnqtjcITfw4PQrkgxDxTOmLmpCW9sV0kTRUxwxt%2FVoFbSFxDZvK5DyCFup0twKfNJ5FbQNOLeqggkB%2FwIY%2FRzn3gwp4yVMc8k4pfn3WhLKWr4VxMGT3zgiDMNZUoo3vMiKZCizmZli0MR9kzTok6mzAkJYh6XAcY9I1m9IjxKweSwW41d10X6X4OcSe4%2Fgc7kB%2BKLQmf2D0Fn6tfQmf5RoPOvR%2FPrA2fu3wPntEkA8r1HNK3CrrvFvxwYSI528RDFPlAfv%2FrvBNy%2BiPMvvi0fv8233vuk7X%2B8H2z%2FfAn68vGK3x2B7jG0cfovXvPdM74P2zzt%2F73VPk1%2BEUfw2%2FH8ZLyozwzXx2NtWoX9bfxl9MHnxvC9B%2Btxa%2Fqfpwv2K73Zb6bB23u%2FX%2FVptMCvbvTTnPoYuMH86kZvhPnNjbYp9dNr%2F%2B%2Bz7OM0%2F5rTDPuGphnzTU0zmqY%2BYNgvZxrBfeA%2B%2FfO%2FzTuK3X3YffLnl51AXva5X7%2FUnMR%2FDJ0h0hXK5ZvOEKTPZcd%2BXZ2hvsLPvOkM6Qgflhg9FvezznA9XU79QZbEU3MjKrtoj1NR24VtLPLLnp074CVd7IplZ9s33U6x5kA9p9cVr6U489QXQ4fqCHZIe4cMK%2BKyMhcP6GJ2uubgrBDu2PAE8l%2FJXqNXpxZxmYG1UteB86kG6dmErilolluO9YYv1Xtc2Io9lDny%2Bl8HbWAG5onUAl6mED2xtqy1SY3eocssgmZT04p6nBuz3kqIBNcejCrShJG5q2WxXI28ZZhZAQrjUeNIMAg9wWHkrWalqDFLBPKCNHhSRzU3AxjLsHq9ED8agjjK8asiS3DgGi5ODQt%2FInOZeiWz%2BBmtGNIc7jEAMo1CkTsnBmG%2F8cqg%2BKing9SS3CU2aJofREunUETPlboxIsQIat6Bl2N3TOUDfD%2FNM1KdUq43hUQQtUkpahYfIn98JoqYzBLfrEubJxE%2BDMVpWDZtp4I0I1a5Y7zA17kOYpnt%2B1xCeb3SgHAvoLwOG1BM37tA1gTYOLrIg9TuwNFF8voFNs5IXocNCA0KH1w6hBGePpDygzCBpw8xwuEMG3uIEVDjAM5yzp8niBHOFRxhcIddVcXX6VPAhswXou6%2Bc1wjqOpuzOducRJTQ2jZ4hXkM9D4HYdUz8K%2BG%2BmdIVQIo79sNrSaaZqHGuCSmZr2IzLyMR8ZRR3hwyIMuGuf1F0j7sbFK3Q3FeJI0DN8RuZYc7oySwm8tDPY3Wl%2FLYvVKnI2Xn1fWiM%2BmMxLUnTS4eKa1oNeZ0IzreouljhpCE8xPnWdsGgEIdE2dlPgvrOLWYmiajN5rOA7G4M%2F0Odz5G4cNiQshsW6pfM10g4mOoqtwDBSAiprnXAJPMWgLC11YlWxCjy%2B7fuxV3SjYw9tQB7WPhlHtjS992VChyFSTimMGjIQU6JFop56o89XhVrWZuJU3%2F6OaPQH%2BzT6JJ2OuP8cmicX7bsrNh1iszM5she5B5UViscqxV4E11VoWnVYkDVCvtlPsMw7bQIxZZec4arkutdBVd5ZplFJOFeDwt6L2kZx843wmuXq%2FnQAoPJthdwZL0tBa1CrVvboUlGFBQKZT6rZuchFE0X9eaL%2BCHkgUA2Blc0RLD%2FEiPzUp9F2aM7O%2BAB39Xzua6MqSuRzWQ8JBfe1G7AKxgQPca9dAp9c1IKMW400og6umXku6pzLdH5Iup4bm2BZ36JWPA90RKBlURln6kwnbccqKQ43L7TrTaSQ698Phf5gn33U4OBF9fUrdDa%2Br7FIbz0Wcr%2Bz0JSt88qsQ2cf8QzFuhJpTNgTSR3y04xOPi7tmUDDqFVWI2nOFRYxDuJmKBLlSzfAMYestcblhCtTUN3dFcvJ89UxJSrKUNSWpZh8OUtuDlhyfI7YIzWDDkxopSlNOlNTvm%2FfzlFcH%2FKeJmlyK14PZ4KJlf23R82%2Fsk98mDO0X4c0LSq4j7tbPJUbUkRNcbc9shGpIyuQmtSGvLQiX9rlL%2FKcwT7sqF%2FqjNjPh64wxJfUAGK%2FzTXwiQoQ%2F5UK8OOB%2F%2FOWQUc%2BN4BfVOmH%2FTbw6G8JfTd3mccb9BWyKx59behLmOWe2qAvV9tahIJnMv7T4JQ4efrKnj%2BFfpIS%2B5A5g2R397Uz70JkNzs5aG1LP0%2BKkFp3dqfdYtxffFxxBvstupqWLAIfDHygdgoAJYt8AVgZWCIh8Z83uHRMi69h2jxJlC1i7J%2FLTkF4Vo6wc3qFWI4p9fKJUVyl1Wjjk8WqyyYFOSiE7kM9kI%2FmSafliDwe2Bav3kJSxl1mi2x6RckZsnEhU0uFoBiJw%2BOowvMbI%2BlLKAB6o5ZUQ48hQB7VdALExcWybCQWLiVMDGcYZnZvqDMkN89V9NwB6xBddWNy7z46TMXNHQXZPDDQCwiS3kZ5REkjpsq70laach1lWTdeBygYNKtHTKcylWgdj9mcNYIby5EYUBGIioNX%2FUrmkG1snlU9ypwhqZrqYh0vIJMJFcJmI2gsNciEffNEt9scirFpUZaZijFhQ3LoLXubTFcVGV5VjEq9B6TjQxeREXX9To1n%2F1Ofx3UYfV7dUj1IhDMGGQ%2FmRmVjtGnyLvC1IbuRx9Eq6Fvs8o%2Fz%2BKIpcb4jpwsR6OwW7yQyKpekJwVkk8lRQnYy3avvCuaQAjcf99nFl6zYsnJCUbUFTimHpS4kCFWFDPPYpHaHZn1I%2FJWs5k4mdAYlPimOwjITjgcX0avdTcqMxcpzCAYVd4XwgPQvoiEhmH1XqGeutaWUVfiP5ULAB82V6bjNmaz1dTVYkQO%2BTxoXxjHgyhyIYQQkmvG5uRuBqKkM0nH8q%2FVBh8u%2FWx19y%2F6Nafo7q%2BPBlGzaP%2BuBJqWCOdDXaQvhQeo9kzKt8sUu0qtlg3nDr%2BIE4evgQIn%2BcBPPG9H5Mj7k%2B0cj%2B2LmGyOrXSEkcHLS2OGOPl%2FcJuUW3LrY1dkSp9PcHG%2FTjLZyM35F07LfXCMdzAZZp57b%2BYRUlNF233GsNVHfHMzZnVNVrpzfkgp%2BajKwOu2boeT%2FrYjvlKa%2FsyL2TMmYo2NYhHXc9GVlajy0ARwvp6YmGemitOSgT%2BqIYl132EQnp%2FV5Pwx7%2FNGo6koeliA3hoNQwZ3eAvOj0QTRdnJuvT0KIo1VTmRYoGqIkyjTdV3rTGh0%2Fp3W5fFIIWlm8C9UnvbfHxX%2FYJ9ugG1uMimNizweQ%2FC7x03xaqL8JUkL5%2F5kgpEUe20CSIkxHQjuFZIrLQmpvYnSh9OFktr7Ic9zBACIPymFA4n%2FynmCpT4DhKkvioJ%2FkCh%2FZKOTm%2Fe4gxcH7MtXBlKkWYL3KP%2FbPp4RrsuoT4BUGyWjr9z5E30%2FYrOCP26Ek2vVwR4aEMW53tng%2Bsia8k5L8jFuD9wJBfW7ID%2F44hSr7D5d54vB9Ak2cJMOCoshaHABrMGWWi7eZ7ikGg0uKXnM0m5L4SPH3Nhzle4CFqnyJnbXVlvEAsIttEO%2BRxs4OrCKUN13%2FN0a%2B4FfBv0A4VD%2FMdZ%2FyN5is3mr2zKdta5FvEGqRl2LN812NhrodBTd9aQOKN6ftxRkwOeDrueGlqH66DiJWlfQip%2BVM8lmsoBS9Y3tmr7d7ProrMFKV8OmwfWWchzrDktcq4RqVfFTxdxOIlUL6Whl704QF5IsEfeyTM8dAw%2FCKXuDUz1KZscnKPTAatPVY17Z1ToNUCR%2Fi44NqrU2xpSKjc1XUcUJNbemPssZeeKXZt5715kEcKtxfEbxKipWNd%2Bs8HrCt9x6ZzoQQ5oazAxtNNbK3lR3sk2dFNsxYUZ8xiFKiFQReeMPgy3a0hyDeEDbJRXD7RLpCqkY6QoXElA60hXCxgE4qHcSbpdOBfew%2FV0DYjWjTHW%2FGFte9yCPQNul6aHt0u6A6aHtMh6A6aDtEjaEr9Knu3JwOg4794Ujo4aHpgOtuNP%2BOF7p4Tz%2FDK4mddkvpEv5qToa2bWYptguaonej6FtkIxc9vmUi1yBEH8le3vSF16hjzI9koV2zCTeYfaH7khNmOLvGTkjVJM35x0u1mpBWDJytbbE%2BVStuVj66Btfqn4jiJ0oqnqSs9eFUss8kyW7VJ%2Blf%2BrYTT2AomaIi2hBOfVW%2BPsXRfLtqsf4rIC%2F54j9tk%2BB4rK7Q64ouaBfYCxwQ9GEn3hJZtyFKwCniZQ7ha4orNNpgR9H9WHPzouKUYSB2tp6Vb9W3F5FXwxJuFRIajim70tlseBSORokUSyEIkEGjuJ5TPOB6zNQ2%2B%2BERn%2B4z%2Fa0cHl4DVssG98NsnA75fNzX5x9pvGLUufrDWehuB2Q7UvtllxfwflG6uIFCuEXMV5Fo0tuSEHF%2B0C9wkdV4Zd9nD2q2KnKs3gjiLdbJzGuImtiWKsXChBko0l3UZStU1bXe5li2nusn3MgwneHZ0nYOpIv3WdkYu3dwF9D31%2Bj%2BhZ3J5uV4g59VtXoTvnfeYR%2B26eGlJYZDtn6Lu1yNJ1BBHcTuM9DiZ6OVjfyGS%2B03LzTghLRLPTJKtdzYz1U8agt7CBWnXyOnDDyT3B8n5nO90lMqAaVbZE8s%2Fj0H6oUOyTJrMBXg4fRzo2800AAHOw7odIf7DMaiQcfi2eUo2hJM%2BKntSGn50tHuC9ML5AoIhUp6buvtQYd5MLsGsevWVEX26HTWJ9NbwYommQSIsF09Nm5TiB7mtMKn3o4mAZvMk1RMkBd0fq5p5y48P2cO6OvH4rFKqya4rNtV5uBN5CG%2FkDxCSOZ%2F%2B3p%2F8s%2BBcJquBtkmGq718dJmaYZnyfmZg8owxRuYniJPTQB9%2FFa0fHahFLqHjKKwNM2pXqmthfz0G4RoDkjkma6HFSyRt%2BdpiuRLxwQ3N3Sg2O%2BK4K%2FxlL5z59y6v1LfEZ%2FYL4sRPuXYf6%2FMVT%2BJoveDxObAMeP%2BICTn%2Fj8%2FjKl3jdgtvxtlP%2F%2FDeVnNSUY84H61eB9Zi1%2B2cH7bczQb0bjO4g0%2Bbeu%2Fdi3FULCItf%2B3%2FXA%2Fyn%2B6L917P8n9gEjaJZmCYbBMRqjd0T6k0%2FIrx1VvpRD%2F7cQy%2FR22V8cZkL%2Fp3MR%2F6bmIvfLufjr6fK%2FBjf9k6Q%2F0PivnKS4Lzv38G8swGn3tWce%2BU3NPCgMfGCY3xVtKPJ%2FnHr4jvpAYtRPUxr%2FupPwo6DwN7dG5J%2B4dfGvV4rpX9caYa9mCd7cuojTypASyjm8fGKNmJ3zIVJJsZjm5OUmQy6swyRMwyJwI%2BBv8Em3%2BjGZ3il3W95xzG5NCTwNeAMQwSJ5LKM1hnpN2o4TgUiiajIkwU2bH6rCnn%2BRtf24NOOIsgOLRZ9ieL2QSo6K6JjLefAZL2KOy60pl8HL8wgQbHdSbOHgTFmdHr0ZXjXRHNeMZYRlKIyIV9%2BSMCElM9KsMPJMZir%2BZkTYobocTFd2nNVgDIkH0Zh4IzJ4sOtF6NS1pbZ0SZt9gB2jLezqKLfTuRywYBklX6xcjnUqfXPkItsKmXOZnZKrD6THKc03fU2VIeMM%2FSIJ1aMzQ4t6rD1e9vKEIpyaFllLRNNBBo6ENeEhTsW9qbFa00bP3rINcBRiQvdQSORD0RCE9zAnFBilEawE7tatzD1JBp14Sh%2FT7FVcFmCkcmasINJ9P3iY1goiTzWTsjwYjC5xlkOYXWF7IeMF5ci9Od%2BlNYmbKGeSil4IeZQx%2FPedyf%2B%2Fq72wMjg4XOv%2BOhiTqS%2BcyAf3%2FvriUhw57ymmVXr8EiBDUCxRr%2FSZpyozjGd%2BImN7bvNYasb9iWT2xX2HYsxEAr%2FrnRS0t45yDuvkEFIQtGA6YN3hMDHqo6PUdtSt040ko4K6gbFx6kzgKcGCbzh0SgOw9X7Lp%2BY2FSfVH5OZd6xUJMdSkqgEv5c6%2F8jEKeH2xEXOi07N9cbijTQqjXty%2Fz6o%2Fmf06bjzlDKEy5hJxOfBQ38ijShWm3qXVN3c0Nua6XrtIAb%2Bvg1IPlBRxTB0Bpu1tDnqi3tojaC0FJ3v2c0SUeaZT61xjnIjPZ%2Bldl7tqE0YtAWcCqPMFwWbV6vYdqZvggpfqGqSmaSTfOyurz4rUVCfOpFT658rE1XMOSJlqi8ygr6iDFS74IaKGoFzPMkZilDCrUW35YcpHfmamjLwzPZbeiP8ciYpazpi82UkJC4v7ri0sBP66UCN2cTVIt8dbEnOfV27tMtdRFtWg5%2Fws7o9hHgajseiVHV%2BXIYI2Q993Z1CR9QjVnV%2FqBFCfd4yb55cmqgJPdEO5dusP7SYohid8Rzmd3V54yEbhBiizMTkfJICsG%2FgOSY7tow5gsUNWisoRUhVNM%2B3ZbF2sY%2BS4Sc5cpumqlwTGCdiEjLJgtwou0nBKLgsFn35FujwZfrU2uEUTz13fSWZir0tCg2xc%2BngvDKRsPhDOF6Xeo5ZcyfG%2BP3xfGkiRxyeO0Y4vcUZ6%2FHuhJ%2FukaAC5P3NXjHQWEIHRKJDLukxN8C1o4hH0uMnkQy12URLDYymk6dKnK7ilE62QsIDLY7K%2B%2FFWsff3EQ9ERq1SjIMPWg8gFsddglaXGLqhmFI3B5mnllDPv0e6%2F%2B99dg7i6MguEdO0yDt65IhS5Gl66pMr4gP4uz0pDnGFX0HgrCAkTAHKy5oEz5kyi2D00abMUcO50lFYbTferOu9ZthxUbealvqFGaYAiY6LOqdexbzHlyNxL0OFaeWKcqgI1cVk9ki9iTo8WAwvsgnn0wp2%2FVIRWSz9uYgs%2BgP9RYsJfQR7n9eOE7%2FWjmM%2FbETWNoC%2FqxLFdp8bzS%2BqKsd%2FkDq%2B8afhWdGjhbvt18XxGKrk%2B47j7SuHqpFlz09wfB%2BdnlvtoPrkYrNC2CfnOcnL%2FeFFuRHugeDpYldOIq%2FvEUZnm7wgGvN%2B5qnuhGUL8vTupgR5IMwdV%2BlgEiQEUBsM5CKZdp%2Bx0rfebvFTtSBHz3iOxhacdeQKNqaqjrvHPqHRrJsGt%2FkOMgRtN1u6VZy9aSYUpASAeyFjNRmqZrq23HumktcA919Ukrfk3h1XPITwYTepKutJ8%2BQSrWn7qjMefWYwiQlMxqE7lL44HqM2i64MNx9PYca6c41CsohjdtW1qT8M8DZzVQ5Xjm49QRcbN5uv1J6lVVVJvI6jmKQ5Bjv7iJJ0ygTVcqvprSy21fuFYLB%2BjFZobLi9IZTw%2BbqzcXMkgL%2FV%2B52kvGIz2bM7MOPxgNwuDWxSOPzGeTkK2nnzgwr8rqJHb2XsjJjZ0biGg2hCfEORWbPVSnl2hgglrfPErGTw9%2Ff1%2BKlPrbm2p2SK2GBWj8FzGC%2FLIFilqdGkUbCoyjF%2FjdXDzfJYp5q1a0FmXMt0uGIsQJ%2BIWWIE5G5onqKowyWQsfuUfR5Jhr8fUZgUcT%2F42uOujXvDKFRTfay86t84isoPY2zkZLG%2Frk8o3K5xMpL5ceyUrZrvenfzyROm0jWnIKRi7s6op5O6PywhvnMgoNS3yq7Dg0%2BPS7DcfH%2BhoMRND%2FEyKd8F3f%2BMPhUKS1s1YlwaEwc6xlMQdqwSo5DFMBoTonkkQJ2KsruABeLEOaDTpqZJOPFPabtLi07uYr3qOuXMeS3HUqO2ZSK5tb3HN0k7Jqy1spn2ntU78GOqM38ob0ws3Hkx2o%2BV2EEA2JIIR7xmguXUyQ0F7aCtbbGKWKUG3YuTezRzsh0r8lYbCDn0RbnZJbec3QkPMzL5FFimRGfw8RsRNM2zbpZ177brneWavcYebhRTPGyqaaupPFU%2B9Wy05i7x9D7XJpAgJzjses8aqTPKwqPW1zo519qn6m29odylnqLjbaN3%2FHdB4T%2Bvz%2FZCjmjGtknENxB7IDrUomHu1lPfc32EAlQ09gxnr0CRjOqjuvNikPHW9TVicJurwW6obdxtjaytWC5GVagj5uIy3Tz08%2FCW7tvC8FAEjMXfO4M1eV%2F8u1P1Z%2F%2FLlOZsbZicm9nRnAU3X9nO2skhXZIoQ50l92dGzKTzwNtZ3ljE7V7DnSKheaBw1UjljVbHujDyLvcY2xl4OSBPVR3d4MEJiChQfQccBpWaluCa4g0a%2BQbe4iF92GJKEghRd5CxUDJKDbPAAWxUkE2HlC2074qOf0afR8zUiJAhQsKdgt2qYHNpPPPVgTwxirLIRXWjkWgkIS%2FhITVnXEtGAqcpsSNj5hZxnkmrDVtxbGNSFjf2yZh7ycLIz33JIphC%2FmUVd%2F%2F56%2BylvweTP6ae%2FEIw%2Bbe5L%2F4VTP5NmZ8fxokMjh%2FxgeW%2BOXD8g4Tc%2BZ8auXe%2BgVyzvzI8xuHnDR7Tj%2FPkb%2FDY%2BAQeJ3HSxsqDP9H2wg0AI%2B4289jnbiUwMS%2BGOZBpcZzuEPZaizNPadyKrqP4Tr9qFBms3GOZSaJmdyyQxHvGJCnYjM8y%2Fi%2BSQilPjPFRvkquYfAdXi%2Bo1I%2BYEdyFqTqsjqfywKbD2BX2AjTSe0vfR16rEU%2FmGF6GZODsxFA4nbHIzlXewfjKri32BozXnmFR2Z4a%2BVCTm3m8fgu4a0NsYYJIDLwR556NLcYN51kNOs8ioBTRvxvJSe1qZ7q71kekkkb3vHbWND55dlbH4SLSL%2B%2BmAxSbYr3aGeF0bKR89CgFvVxH69KStwvg2dZD7vhqjLTbnNchC8TLG92pNV0uBhlaTKWlc2sar3ctt3J0QjSiJFeUK8%2F9pE3R2rE%2BMse1baG3xVslE2sLtItRoB1FcdlWS%2FjKZGFBxLVbh8WQNRRrYrgrWijQzpDwtEOBdj9IIjC3x2iQJbWqJ0UzJJE2mSSSzHVSaymkM5kF97qQhtAJz6cv%2BjZGkkLfz89JYwVv3EfscfEXAawzHH7ShuwWSTclw8ZIX0HUij2%2BBUfwFwLy6W6fvL2VSvJSklXr%2FYiv9%2FQ%2BYm3POOCQ6WzDenIzyoKr%2Bjpv8SfugVVlt%2F8uqfs%2F9XnETY0OnkN%2FoQfVqPPdWwmfNGAalK2IJi6APSQTStVCN%2BDCjc4u0Y0q3rOflLZqRB2VtnopcU%2BPEXM123zdrbaxoihdq8CHdQpQ6c%2Fnsy4WGSTfwHt%2FkT75kPAePIeKR7NWmwbUOPDasGRyLO6tgNS9p2cugYhLlKJnJ1vl6%2FDM6EIz1v4Bboy6rIArv8zTAW1ousi781I0s%2Bnup1DqmRtDJeXTOtwsGa2LnUAGaDsrpt0yBbM%2FSJSf2Oy%2BsmoHzERBili6F54bFG6uJaFJSEUl8wuqqnYY5ai4h7Y%2Bq1xOaIXpqrbFS5sDR1DWoT593yPxX%2Ff5SrxpdhKzxzol0ec%2B3nKTxMyK8p7yBI59zE5SHBFtjuqDEZonHUfaw2A4qyRNsIgoMSf8hFeW8%2BEF2Aaxg7oOPWTBzkoqricCR85QjmHdtxSp7Vd%2F8y%2FSJ2a2rsDkKrnmw4h8mCy0VXDUIVlKBJHvk4wmMSd3DCi1TptP3v6BXMyosFrjvTLdGmZ2B3MqIt%2Fcv5ml%2BRjl6SnyE7nl6pb1O5Td9Au7UvTcScUFzWq4cuQL%2FD7p8UFgQdMkKKM334uzXRW4CJxJSqm7NuvuoO9XecxJP6ln1xMOeAq4Va%2FGrN%2F53zJl%2F4pdTL1y%2Bo44t4knNisIvRqOXwm554qSNPRRC0wwsieUNs59MVmjEfMz%2FytzlxDUf4KFqQ8U%2FUWx8G9j4%2F6WWAqVJZW79xIInuTa6VdGUoRZAvzN0Hh4Ji%2F0vLnzaQmE6NRGykM81WeLsAu4gJOdQkjey%2FT2XpTrhA2kIbcGqXAlpSgLtnia2FPKa0mzs2zALdzX16gMI8IBm1mnzTAbgJ7RKAL3fY6T%2BFweGYqOt9IINrFlDTIB32xZg8wta1CKGihrULJlDdrxSrJlDSJBHaaVhi29M3LiTscgZIP32dKeIL%2BPfdvE8NhcBxPFjcH5uQBxwme8A4FGJk22uy7uC%2BGrcV5Xz1gZwiOZSSRR8bQbi7KeWcj5p2ypHKEPsh%2B76tWPxUKom9sJxy3x6kK82FzXcPLybNt%2FtzQp3L5TRo%2FhTG903l20mLmMKZniIyJ7Ra4Q81y6Jaa2kPyN409t7ynWodoyEsqjHYLolmBc5q3kIM9X5LaFPE0I5sFo4ozpAxEN1CmaQGgRLko32XQZRoZ52HhO7D12tQ7UfrzROoJyfGMgQBUQxGjZfq5nNYcobUw780VdgJjv0mjFudF3NdJgINR4K1BPTcuWGn57WdzraG1hxx4jNRE%2FMoRNZpscm5XsTklRWQaSaXz4lrsJ7oPilhdKzffrlhdK3fJCGeDU%2FHcjrCRbXih6ywtFogbKRbVDuahQifLdVqI8hytrK1H%2B5ftEvNdxBKZoID82B44YnlTGqyeUW7IvWVaaGp2BOOlOHpzHSj3C%2Fchll2IGmcPfFDoqfZv2Ke%2FZ53tk2OGnmVwcwq4VPqxrMLjSYV1PAJnq7ywu%2BxtoMy5Jy3Krk5%2FH3pgdnkzKwrEKW79jOxI8cGnM0xkfprsJpplQw%2FhF7Q7FZN6P%2BkW8Y71WhyKcM5CB5670hD89Lk%2FqATvS46Xs47%2FV%2BPzLPsXVsCI1iboeYyVR5xtL55%2BJfqpTzsvZbXbLmNvAWz10Cn4q9cjy9wPcZpqKScnBmyIsarlM1A%2B54Tzvxto31swxnRXgXkUlUUte1C6B8uu8RDXY5NUG%2BeTLqi4WKRRa739r%2Bv7Up7hyhq7lUryWg9WszAinHkQJ7Y5s9pVIDeaF1sF1bpTd3REPnrCWKdi5UrGSVhXTW07c%2FYPLNPjUQ6AYxTIq104YyzDci1dGmHX9omtmmorVylO5lqGHIVaHqNzKNK%2B0WHghQ8RNTXavDXVjM0iG%2FdEoxKr250YNpx9hFH7uE877WIISaF9NqsieOl1PkFH%2BnhjbdJ7ZqzIWdpIbz6I0qlJgTw9Qx%2Fe2iVKiJ%2FKA0EYsLXdbdtDKaPLGwlhGJ9IdUVFp1KA1Y%2BMb2FsY5fCuszNZb9JRkiEdA9Lfm74%2F93mwLAYH6WqaiIk6GUOETCp4McoUbVE6n%2BhKnJ0ifbKbs%2BHk697bj%2BRwmYfD6l9L7jGu6pFLfFnnq%2FaQeYJPB3Oe%2BwIUJ5yjieFCgXbyJqcdXompXVAVN7Gsm5xiUVq0HGn5gKpeWQlxEGlyGsRaohuq%2F8OL1QnEbnxn1fHO7Q59sUdJPVz9GK%2BWeQ2%2Fabr%2B%2BX1SdTPcUgx3kSMxvt8SnAymg9yM%2FBaVcul8XHpLLPnXmClJ8j8zU3L4F4Vm%2FzLXxf%2BZKT8dP%2BLD7pcVFr4FM%2BW%2FLJH7f%2BP3s2aE%2FFnr8Q0N31fMJfG7RP23Ufcf9TnfSNQ9xv0qTuLXu%2BV%2FnOEBZ1E50l%2FdjfrV3f7i6PqP8%2B%2Fvn14E%2B0%2FL2H4MVPhG5hucJJ8meWB%2BNV%2F%2B51w3BEZ%2FoIhPskf8crtiv3AxZeI%2FSPPwo01E7JuaiFu6EXb3O2lB%2FveJSEEplPw5dAmjya87EX8bcfY9MMlvK0HXn8Yk0aQj2E9y0eBfd3L8IEFsE7It3d9tS5d8jxlf17Z02Zml9JYaH0%2BKVUWp8XPqF156Z81T7uKJqXo64WcvDEQ50HnpcUoaMuj4yzXnTSAboNiBbNi8nYIwV2gUACF6pft6tstZ4XfP4dUiV7jGCdWZTvuHASwR5UFprCdvi1M4gxjwxy3IGDb2xIFgZmsrGz0nmbXuuCx73oBVEubQHSmU%2BmVLF1PQadPO1MoDZAtiMuRS51%2FbqQEYcbzzd%2FE2sUowcK2fvdl4qAyZuLIEucD5LJuhw9QDeEjZknEEwGuW6CSGeg92iwaZY7PxTCTMWrGMcVpXgjCeHquCQ4aRd11E6XNOu83jL7XUrczm1KK751Oy5SP2RQ0lmnld8CpWqB5Q1%2FU0XkMyy42kN54jCqQr2JXdscaTq9LUYlA6B5VrOFON4IpXYiFWK1Rn6sSYhJ7mHCGRmbnELUpik1KcY6Ga4H0LGp5bR0ZeMTOCB%2BrulF5Yexz2GIjyeCRj0TYPt8lTZDDybe1g55SY2fKQ8f116K8dCnbAzdrGTDze9N%2BHhSwYI23JAYuBWYenF75pDK323Zp0mZhmWne%2FGDkBkECIt%2FBwcosKJz82JiA9tvDwaQsPz8Fh2kLScxSJrv7UAOCco5D0ZgtJNwF8LRSSbm6R6OnHxlfq80BUGAOM06jGSdknzyTlq%2BSu6rHnUZ1VDDKpjZE%2B7wahw%2FlnbhXYGu14NgwlP8it20rca8HEFMc%2FkYLV7TNdCsiA932aIvn51u3miTxgncavoUrrlPMcGzWn2Z1HrtKpM62APUS7mynYNJtfdhKBltRJec6HSC5vgrlj24avLZ5N5yVmDSada4DhA0VkO%2Bclkvo0HfVplqn5ZlVMcwb4V6bml%2BtzNogz4PRdlY558cyN6vluDapfmNJG8M%2FOjR4oZU0TkKJrYvCZVpkpLHGrJdiNOf7C3Bcu%2BSuI1BWEDWMmpSIx8YTVI8ZewwGojqHtyGMpRczhbjhlHYu75PV3oeC%2F79MZtBYH4eqaJPu2eyJNukDTEiptJbOHJ7mqM9zqOTle4Q0UP5QPaShgy8LpsXLCC2UGCbMl6lLC4zyTezbtV16JsKkxwbM7xhNJyAHcqHBgrrcLqePTaxUlkRUVQWctBbTrlfRjeZQl7lAW06Ho9me0R71WXaImEdl%2B6QN%2BnFw0jgFbmaLe7etpVuZJbPRlfXvs4vsdg%2F%2B2T4F0iWdev4JFTSa7Y6Uz%2FDw7Vg7aayQm7dBj7N7Q%2Ba7TTwMbjNIWvMjHm7%2B6TCBG1x808ojCxVcRPvfmNytrlQfE62u86mCuc9xi8KzMCIKLk5scP7PrSLwXqsky6RgwWHogR%2BQ0eCcczjw%2BZmWZgtUng%2BBV%2B1m5IjuJSFb84zuj7v%2Fe5y3qNQ29dViaOvmeICWJinQslH5nbgXAQUfCZZHVxlOoBEtulTibQ5GpxzzTY9rBhaI7TmZsN7wl8YO4mvJRRMnmMBzJI8lEAsR9lFaZaKqY9Izc5QZ67tUSBjmF51%2Fh%2BUytAigkmKLR7W9woSCfWuRw09vfPA3%2FtD6Nqbcc3rgwdzN6lG884uAE5HFGNXUYIgla0g59MQg7FHeBmLKoIgESOf3by6Ac1CmpOuOZ%2BDwhOlm7hTW2%2BVb7KWOXVBkCaYBA5a%2F0KmTxD79KXoIRnzNesR%2B4z%2BTcxzjmA0v8Pl79Qwp04rdhdsojrDb8F%2FZQuN19Yg4hf20O2f24yWngkO5%2BPzkNgf88Zl%2FNOEL8ICF4yOgs1%2B8heMcGX5avDO1xs9Tfof1ND3NUPjyNfob2xOljfhpz6emHjdMfy4cXSZeLVwEIOMikdvJXXEAW9mjNqdP0lB5WSYsMOyC83YhVWBMuRShA3BKsYhg9XQBrsflx25NdULw1LtvmfOeFC8preAiRrV6mR4JZkGKQR0k7EkcCmYxryXJjiJSs9sd0tNg%2BnoBImsVMgUAgzVupmmSDpSOxUNRr1DIsenKsOhkpkt1GtZzpjhgbguEGkmiTrL3ukvzJpd7YBvee6xHuV8cmnBwUU%2FVCGcOyN1kGtugHnllv6frQ%2FzvcA6MUrFhrYlOJ3DSuFXcQxC1cJU%2BWyHsZtma7KPTPZw8sjdA%2F%2F5a5BmsOAWkftsw16yPhRDNCCgsaIPdA5FKa1fZopYbNZzOG3E95bByOOUgrjhPBWTjxnZcIsVi6j908Q%2FazI3FviggURFiKmsW7EH4fzqxFRVnEnAlvOhHBVhew3PQiFJU8u1ix8UG3V3ljZpCrVRsDhSNSbQz0X42RAKCwddkY6GPjm%2F7Hho0YKGwcbMRABcgubcRAzxvflH9qfKU%2BX1g3kgdK3622WbBmX7FSUocRXB4elSuuwPYjNefyauEi%2BbBN18z2oZHXIH8BfZ5LXZ%2BTSb0ovEjsG4FKqCLXRlOkMmk2SUeG4kITV6yqmKMi8LXOY8RR0bGZDZJ25V9Rbd2pzqiF%2BDFNEW%2Bp6AT1zl%2B%2Bb5r%2BF33eEm%2FZMl5y42AzQ22gAtBNjmlOxNg04eU28Ci21CY4UquqpOqTHkZpGcQ0Wt1Q96FUteDLRJmXYGlCZkwv9CBYaGJ7JGu94zPv0G3ZL6u1XMDtm3r%2Fv7BPYR7Gi8B0l51zRnudSGYiyjkzOrfkdrVqwOizg4kKUgvKJCfJedNW%2BdrPsSZ59d1Z2XuQ%2BgDl93az1PaSpZzELi08YV9vwakXAp%2FCVWwyTZnSRmwH5Owc3eSdFBg5Ude2mvocRzKpkj38uSAn8IBv2rHHe1I9b0Zqo32NUi%2BkapB6sXbuXIIIlQRnZ4Rg4ELx%2BUMYQDHZL6M4Tm3lOxyFP9DnayxR9hIUzZCxPRbrmc7fUUBquvHQwbogBTetwg3jLt8MPY6cHWcaFatwqMajPy3rdO3rfLmMKyZsqtgd8opOcCSgICFa3rLRpF4YqfzdaEvpfoq%2FLRr8hX3eEreXoci9Wx1jbFhStZiy8gRrHTLRE%2FmmvoWrbp%2BqJL%2B5e7iB1El3j%2FglRunkZHaiVE85dQorq%2FiNe4u1AyJzzEbVnWaOmgJNJFMog7SWFBxoJD0oATDNOBCqWb0AEQUGWE3ymlmcV1zdPwmAZoq1OcePTgerrN3MB1giXocjXnCF0zBz50p%2Fu1H4l32ah5Gmzmdxd%2FFT7y9004TY58Pu0xIev3L5%2BzzypT580RysxA8SULcZPds3ZCRWGJJP%2Fa%2BPjS7Eho1Y%2B4o3aCbm0ydmz8JJDV%2BR%2BFO6u%2FT2PD7znHn4%2BesmcI%2B9GJ6BbIqcfPZtfJE673BMYvp8EvQ6RwmGPQcltsyp0hj7pHgA8jByLKdrwBTHTd%2F0u2qmOWEHjXmTcQaHgUgdf0tRgmSeOUlIF6IlLgMqqinLeakv8Czfxy%2FISM2DljcmKbWIlY9beFvCVusZ2UORQGCxfGyMKaEbVNq8wixRkd0yUIkTwgxvCKi%2BmQTJJs%2F1zEQRk7Zt1ftHKAxvxTJEwLybRB2M2bHjYeHytOdTm2FGT29PJqBXjzlGrsWb%2Flll6tuQnLx2VgAS3qwdpzrBTO9hmyYAm4wzubYVYyTsSctBiKybJNPolqdOBCDMsbYbB0IXgaBDLdcUgjyvKrXqLMvNN4A4nzMiNV%2Bm9pN3lIAOpvaEt9aWkqHQ21xGtTAVEK7TuV6noBWz45pORMVmwupOOYGqm4hZuyExyFtRxeNWrFNxU4x%2B08rIP7XPEinyM1to%2Bx1ZdvrOQVCUE4%2FM3txTo%2FrcTJo7LYeiJQojFDr8gIyazJrtBPIZn4saBS1oVmj38%2FLUIuGwyZeylZ4vpPBubiQWCdcnR7VyKxIWNlkLJaZmfCl3yF9g74jBbY%2BPasxKBFmkl34ipT0uZXl8wp8TiOTidjZ3LLYWmpinahc36gFuCPqkQE5PKfRu5ZWUt13FHFwBhbtfyx%2FNtBnemTFpq4dqsAGy1HSdYs%2BQ2RpBvxWc4a%2FhwMtQcrzW%2Bfpm3NQ24%2Ba2XNgRLpcJrzfjZtisAC6X0ZxTJOM0bKbMLugIX8ui0bm%2F4M3jGhDuW9ma%2FXr5bun2X%2FfZoMUy%2BnxrPJiS5jLHsIj8%2FODbhJkzVduybsHTBTaYDaEEp3QKaLgq1hOI8iOipZBnubDWR2%2FxyeM0mfG%2BIZ6LYZ458tyAi8IzN5RTNJVYjgCuwtOgXS4kkLmcdi20UZvyPop9iP8ykSQfqqtYmSlxk1zkF1LW8NJ7G9tvjnJ%2FqaFswA5ECrfzixk91s044%2BvVLRbDaIVbPMMOWCxYb0ir7jZm6WqrkHoIKonPjNeSojM25xfMrG04s82g5E7MFgxmlN0pGCaFJlLCuKAkKTo%2FdGZAWif88d3S7L%2Fuc6t4n%2Baq9%2F%2FaO7vmRGEoDP%2BaXtYhhJBwCdaCrgoWZtW9E0r4rlYrdv31JVbqCDjtTivarReOTmDIZN4nkSTvyZkoa413JYN7NlNfTTka4p4yMlTHGth4FephN%2FKH4%2BmAIhdZjqWuHlI%2BgIkObrDsex0SGyBI3KYzHgVyiDt0rumR4rvj2SKSNHXSWY%2BS5oK0ZfIHYd1QkOcZq7t7xF5Q6CxGTagMh8rAay0FEgLD0eUmXmoyerUHtE2yUrWsl1hpPO7L35%2Ftf6nTsSmf%2FRnCR8lWQqtld2%2Byz23UWyeTtUptTO1oaE%2Bt1%2F7R5sL%2BQDYD4AgpxNKvJ6qoJkm7pLdy2UL4MqA00h9iyjx7t77xO5F82BdabB9gLrrxzN0c%2Fw4XlMYIzow50nhkLGj6lxnP%2BDuqLIkyZM66Wg9KOTCvq3dWV47F%2BwY%2BZ3hewRmgkHMTcMX0wB81OgORe%2BdJx7Y2nzCV9Sd4OK%2FgsLfu%2BmkeeE5sILxLXE%2F2je8AFLO7HhuPH5OHOm%2FY%2B%2BydV8wFD4rsFTP1fpQ9AcPGfvxG7bjl1VVHGpesNfwPjjQmRa1g1ctFrV4aoRzMd1HvwAYAd0Lx7rrzIHVixTSh5Mlxf5Ag6brscbvixfhp2%2Fo9VcTH5TS%2FcL0I1lmpzAQms%2BfdxeyXt%2F3ePMXOC7i8hJl2inexidSmurz4LHk4oHcFFQcRKBEglAEQ6tS%2FygdXUO5rgAAHta7C4n%2FVH4iNQky3wJ2YgKr9vqOMAPxlBLjaje5b%2BUVyYvmrFgaOIj%2B8yM%2B0fdvO3wIgVRwUUysAVSsBRwFAuADA%2Br%2FUwAXfB1%2FxFvhFCLCV0SmTZTddy9rl96b3LrvjBQ%3D%3D), [png 200%](https://i.imgur.com/xbjECxq.png).

**b. For each of the following heuristics h(n) (where n is the state) for the N-puzzle problem, identifyits admissibility and justify your answer.**
**- h(n) = 1.**
**Answer:** h(n) = 1 is not admissible because at goal state, h(n) must be zero.

**- h(n) = the number of misplaced tiles at state n.**
**Answer:** h is an admissible heuristic, since it is clear that every tile that is out of position must be moved at least once. $h(n) \leq h^*(n)$ .

Proof: Let $k$ be the misplaced tiles as state n. So $h(n) = k$ and we need to proof  $h(n) \leq h^*(n)$.
In n + 1 state, there are 3 case can happen:

- No thin




**- h(n) = (number of tiles out of row + number of tiles out of column).**
**Answer:** h is an admissible heuristic, since every tile that is out of column or out of row must be moved at least once and every tile that is both out of column and out of row must be moved at least twice. $h(n) \leq h^*(n)$.





====== END =====