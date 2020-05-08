import tensorflow as tf

from trace_generator_card_matching import generate as generate_card_pattern_matching
from train_card_matching import train_card_pattern_matching
from evaluate_card_matching import evaluate_card_pattern_matching

FLAGS = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string("task", "card_pattern_matching", "NPI task-[card_pattern_matching]")

tf.app.flags.DEFINE_boolean("generate", True, "Boolean whether to generate training/test data.")
tf.app.flags.DEFINE_integer("num_training", 500, "Number of training examples to generate.")
tf.app.flags.DEFINE_integer("num_test", 100, "Number of test examples to generate.")

tf.app.flags.DEFINE_boolean("do_train", False, "Boolean whether to continue training model.")
tf.app.flags.DEFINE_boolean("do_eval", False, "Boolean whether to perform model evaluation.")
tf.app.flags.DEFINE_integer("num_epochs", 5, "Number of training epochs to perform.")

def card_pattern_matching():
    # Generate Data (if necessary)
    if FLAGS.generate:
        generate_card_pattern_matching('train', num=FLAGS.num_training)
        generate_card_pattern_matching('test', num=FLAGS.num_test, only_random=True)

    # Train Model (if necessary)
    if FLAGS.do_train:
        train_card_pattern_matching(FLAGS.num_epochs)

    # Evaluate Model
    if FLAGS.do_eval:
        evaluate_card_pattern_matching()
        
def main(_):
     card_pattern_matching()

if __name__ == "__main__":
    tf.app.run()