# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kle-scor <kle-scor@student.42nice.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/25 11:34:22 by kle-scor          #+#    #+#              #
#    Updated: 2026/03/25 11:34:25 by kle-scor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    x = int(input("Enter plant age in days: "))
    if x > 60:
        print("Plant is ready to harvest!")
    if x <= 60:
        print("Plant needs more time to grow.")
