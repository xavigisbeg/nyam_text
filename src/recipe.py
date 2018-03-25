# -*- coding: utf-8 -*-
from transitions import Machine
# from transitions.extensions.states import add_state_features, Tags, Timeout
import yaml
# import logging


with open('.\\config\\recipes.yaml', "r") as file_descriptor:
    fsm_data = yaml.load(file_descriptor)
    fsm_recipes = fsm_data['recipes']
    steps = fsm_recipes[1]['steps']


def create_states_transitions(steps):
    transitions, states = [], []
    states.append(steps[0]['name'])
    for step in range(1, len(steps)):
        transitions.extend(({
            'trigger': 'go_next_step',
            'source': steps[step - 1]['name'],
            'dest': steps[step]['name'],
            },
            {
            'trigger': 'go_previous_step',
            'source': steps[step - 1]['name'],
            'dest': steps[step]['name'],
            },
        ))
        states.append(steps[step]['name'])
    return states, transitions


def instantiate_states_machine():
    recip = Recipe()
    machine = CustomStateMachine(
        model=recip,
        states=recip.states,
        transitions=recip.transitions,
        send_event=True,
        initial='step1',
        ignore_invalid_triggers=True,  # Program not aware of state
    )
    recip.to_step1()
    return recip


def run_all_steps(recipe):
    for step in recipe.states:
        print('{}: {}'.format(recipe.state, recipe.get_step_text()))
        recipe.go_next_step()


def steps_to_dict(steps):
    dic = {}
    for step in range(len(steps)):
        dic[steps[step]['name']] = steps[step]['text']
    return dic


# @add_state_features(Tags, Timeout)
class CustomStateMachine(Machine):
    pass


class Recipe(object):
    """Self-configures with the loaded steps"""
    states, transitions = create_states_transitions(steps=steps)

    def __init__(self,):
        self.recipe = fsm_recipes[1]
        self.steps = steps_to_dict(steps)

    def print_recipe(self,):
        print(self.recipe)
        print(self.steps)

    def get_step_text(self):
        return self.steps[self.state]


if __name__ == '__main__':
    recip = instantiate_states_machine()
    print('{}: {}'.format(recip.state, recip.get_step_text()))
    recip.go_next_step()
    print('{}: {}'.format(recip.state, recip.get_step_text()))
    recip.go_next_step()
    print('{}: {}'.format(recip.state, recip.get_step_text()))
