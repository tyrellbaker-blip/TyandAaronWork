class LightSwitch:
    def __init__(self):
        self.switch_is_on = False

    def turn_on(self):
        self.switch_is_on = True

    def turn_off(self):
        self.switch_is_on = False


def main():
    kitchen_light_switch = LightSwitch()
    bathroom_light_switch = LightSwitch()
    living_room_light_switch = LightSwitch()

    kitchen_light_switch.turn_on()
    bathroom_light_switch.turn_on()
    living_room_light_switch.turn_on()
    print(f"kitchen switch: {kitchen_light_switch.switch_is_on} \n bathroom "
          f"light switch: {bathroom_light_switch.switch_is_on} \n"
          f"living room light switch {living_room_light_switch.switch_is_on}")
    bathroom_light_switch.turn_off()
    print(f"kitchen switch: {kitchen_light_switch.switch_is_on} \n bathroom "
          f"light switch: {bathroom_light_switch.switch_is_on} \n"
          f"living room light switch {living_room_light_switch.switch_is_on}")


if __name__ == '__main__':
    main()