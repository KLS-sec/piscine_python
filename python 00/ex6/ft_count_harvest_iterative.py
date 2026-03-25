# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kle-scor <kle-scor@student.42nice.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/25 11:34:45 by kle-scor          #+#    #+#              #
#    Updated: 2026/03/25 11:34:47 by kle-scor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    x = int(input("Days until harvest: "))

    y = range(1, x + 1)
    for n in y:
        print("Day ", n)
    print("Harvest time!")
