# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kle-scor <kle-scor@student.42nice.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/25 11:35:03 by kle-scor          #+#    #+#              #
#    Updated: 2026/03/25 11:35:06 by kle-scor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit == "packets"):
        unit = "packets available"
    if (unit == "grams"):
        unit = "grams total"
    if (unit == "area"):
        unit = "square meters"
    print(seed_type, "seeds:", quantity, unit)
