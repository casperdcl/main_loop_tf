import gflags
from main_loop_tf import gflags_ext


# ============ Learning
# optimizer_params --> make it a string and parse it?
# class_balance=None
# gflags.DEFINE_integer('BN_mode', 2, 'The batch normalization mode')

gflags.DEFINE_float('lr', 1e-4, 'Initial Learning Rate')

gflags.DEFINE_string('lr_decay', None, 'LR Decay schedule')
gflags.DEFINE_bool('staircase', False, 'Whether to apply decay in a '
                   'discrete staircase, as opposed to continuous, '
                   'fashion.')
# Speicific Piecewise Constant
gflags_ext.DEFINE_intlist('lr_boundaries', None,
                          'A list of Tensors or ints or floats'
                          'with strictly increasing entries, and with all'
                          'elements having the same type as the index.')
gflags_ext.DEFINE_floatlist('lr_values', None, 'List of learning rate')

# Specific Exponential Decay
gflags.DEFINE_integer('decay_steps', None,
                      'How often to decay the LR [in steps]')
gflags.DEFINE_float('decay_rate', None,
                    'Decay rate at each decay step (0,1)')

# Specific Polynomial Decay
gflags.DEFINE_float('power', None,
                    'the power of the polynomial decay. '
                    'Defaults to linear, 1.0. Usually 0.5')
gflags.DEFINE_float('end_lr', None, 'The minimal end Learning Rate')


gflags.DEFINE_string('optimizer', 'adam', 'The optimizer')
gflags_ext.DEFINE_multidict('optimizer_params', {},
                            'The params for the optimizer')
gflags.DEFINE_string('loss_fn', 'sparse_softmax_cross_entropy_with_logits',
                     'The loss function')

gflags.DEFINE_bool('stateful_validation', True, 'If True the state of '
                   'the RNNs will be kept to process the next batch (if '
                   'consecutive)')
gflags.DEFINE_bool('use_extra_BN', False, 'Whether to add a BN layer on '
                   'the input')

# Regularization parameters
gflags.DEFINE_float('weight_decay', 0, 'The weight decay')
gflags.DEFINE_float('dropout', 0, 'The dropout probability')

# Gradient processing
gflags.DEFINE_float("max_grad_norm", None, "Clip gradients to this norm.")
gflags.DEFINE_float("grad_noise_scale", None,
                    "Gradient noise scale {0.01, 0.3, 1.0} ")
gflags.DEFINE_string("thresh_loss", 0.7,
                     "Do not add noise if loss is less than threshold")

gflags.DEFINE_string("grad_noise_decay", None,
                     "Gradient Noise Decay Schedule [neural_gpu]")
gflags.DEFINE_float("grad_multiplier", None, "Gradient Multipliers")
