<div>
                    <button class="menu-button"><a href="{% url 'update_menu_item' menu_item.id %}"><span style="font-size: 0.6em">Edit</span></a></button>
                    <button class="menu-button"><a href="{% url 'delete_menu_item' menu_item.id %}"><span style="font-size: 0.6em">Delete</span></a></button>
                </div>