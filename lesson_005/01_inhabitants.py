# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

import room_1 as rm1
import room_2 as rm2

inhabitant = ', '.join(rm1.folks)
print('В комнате room_1 живут:', inhabitant)
inhabitant = ', '.join(rm2.folks)
print('В комнате room_2 живут:', inhabitant)

# Зачет!