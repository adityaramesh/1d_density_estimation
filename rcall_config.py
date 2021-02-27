BLOCK_HOST_MAINTENANCE = True
CODE_DIR = os.path.expanduser('~/code')
CODE_INCLUDE_PATHS = ['1d_density_estimation']
CODE_IGNORE_PATTERNS = ['.git']

with open(os.path.join(CODE_DIR, '1d_density_estimation', '.gitignore'), 'r') as f:
	for line in f.read().splitlines():
		line = line.strip()

		if len(line) == 0:
			continue
		if line.startswith('/'):
			line = line[1:]
		if not line.startswith('#'):
			CODE_IGNORE_PATTERNS.append(line)

EXTRA_SETUP += """
	set -eux
	set -o vi
"""
