### Use following code as an alternative if needed for the "enemy_attack" definition.

if enemy_attack_choose == 4:
  print(f"The {enemyname} uses the base attack.")
  attackpower = baseattack
  Hero.health -= attackpower
elif enemy_attack_choose == 3:
  enemyspeed += attackpower[enemy_attack_choose]
else:
  print(f"The {enemyname} uses {attackname[enemy_attack_choose]}.")
  Hero.health -= attackpower[enemy_attack_choose]

_**Note:** It is **recommended** when using this alternative code, you should ignore the "enemy_attack" definition and place this code in the "while" loop alongside the hero inputs._
