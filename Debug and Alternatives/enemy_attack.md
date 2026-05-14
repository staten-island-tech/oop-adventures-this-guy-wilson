# Use following code as an alternative if needed for the "enemy_attack" definition.

**Don't delete this file; is used for debug and fixation purposes.**

> if enemy_attack_choose == 4:  
> &nbsp;&nbsp;&nbsp;&nbsp;print(f"The {enemyname} uses the base attack.")  
> &nbsp;&nbsp;&nbsp;&nbsp;attackpower = baseattack  
> &nbsp;&nbsp;&nbsp;&nbsp;Hero.health -= attackpower  
> elif enemy_attack_choose == 3:  
> &nbsp;&nbsp;&nbsp;&nbsp;enemyspeed += attackpower[enemy_attack_choose]  
> else:  
> &nbsp;&nbsp;&nbsp;&nbsp;print(f"The {enemyname} uses {attackname[enemy_attack_choose]}.")  
> &nbsp;&nbsp;&nbsp;&nbsp;Hero.health -= attackpower[enemy_attack_choose]  

_**Note:** It is **recommended** when using this alternative code, you should ignore the "enemy_attack" definition and place this code in the "while" loop alongside the hero inputs._
