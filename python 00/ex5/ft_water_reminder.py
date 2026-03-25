# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kle-scor <kle-scor@student.42nice.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/25 11:34:31 by kle-scor          #+#    #+#              #
#    Updated: 2026/03/25 11:34:34 by kle-scor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_water_reminder():
    x = int(input("Days since last watering: "))
    if x > 2:
        print("Water the plants!")
    if x <= 2:
        print("Plants are fine")
