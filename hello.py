import matplotlib.pyplot as plt

# Data for the pictograph
initial_defenses = 20  # Initial successful defenses
post_training_defenses = 50  # Defenses after training
post_simulation_defenses = 80  # Defenses after simulations

initial_failures = 80  # Initial failures
post_training_failures = 50  # Failures after training
post_simulation_failures = 20  # Failures after simulations

def draw_pictograph():
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.barh(['Initial', 'Post-Training', 'Post-Simulation'], 
            [initial_defenses, post_training_defenses, post_simulation_defenses], 
            color='green', label='Successful Defenses')
    ax.barh(['Initial', 'Post-Training', 'Post-Simulation'], 
            [-initial_failures, -post_training_failures, -post_simulation_failures], 
            color='red', label='Failures')

    ax.set_xlim(-100, 100)
    ax.set_xlabel('Number of Events')
    ax.set_title('Impact of User Feedback and Education on Defense Rates')

    # Adding labels
    for i, (defense, failure) in enumerate(zip([initial_defenses, post_training_defenses, post_simulation_defenses], 
                                               [initial_failures, post_training_failures, post_simulation_failures])):
        ax.text(defense + 3, i, f'{defense} Defenses', va='center', ha='left', color='green', fontsize=12)
        ax.text(-failure - 3, i, f'{failure} Failures', va='center', ha='right', color='red', fontsize=12)

    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend(loc='upper right')
    plt.grid(False)
    plt.show()

# Drawing the pictograph
draw_pictograph()
