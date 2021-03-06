from os import path

'''
USAGE:
'''
template_pip = """# Comments
# Do not remove unused parameters
# [Required for all] input filename
{inputname}
# [Required for all] file type volume/cloud/sc/graph
{type}
# [Required for volume] Smoothing Sigma.
{sigma}
# [Required for volume] Weak threshold.
{densThd}
# DiMorSC parameters.
# [Required for DiMorSC] Persistence threshold
{persist}
# [Required for graph2tree] Root
{root}
# [Required for graph2tree] Saddle threshold
{saddleThd}
# [Optional] Component size threshold. if not specified, the largest is kept
"""

def getLines(file):
	rtn = []
	with open(file, "r") as fp:
		line = fp.readline()
		while line:
			if line.startswith('#'):
				line = fp.readline()
				continue
			# readline has \n in the end
			rtn.append(line.rstrip('\n'))
			line = fp.readline()
	fp.close()
	return rtn

def getPipConfig(file):
	rtn = getLines(file)
	print('parameters detected:', len(rtn))
	if len(rtn) != 7 and len(rtn) != 8:
		print('[getPipConfig] incorrect config file. See config.py for usage.')
		return None
	else:
		if not path.isdir(rtn[0]) and not path.isfile(rtn[0]):
			print('[getPipConfig]\t', rtn[0], 'does not exist')
			return None
		
		# TODO
		if len(rtn) == 7:
			rtn.append('-1')
		# check sigma should be positive
		# check filetype should be volume/cloud/sc/graph
		# check densThd should be number
		# check persist should be positive
		# check root should be a list of length 3
		# check saddle Thd should be number
		return rtn

def getDefaultPip():
	config = [
	'data/Olfactory_OP7_trunc.tif',
	'volume',
	'2',
	'0.1',
	'5',
	'0 0 0',
	'0'
	]
	return config

def writePipConfig(filename, pip_config):
	f = open(filename, 'w')
	if f is not None:
		to_write = template_pip.format(
			inputname=pip_config[0],
			type=pip_config[1],
			sigma=pip_config[2],
			densThd=pip_config[3],
			persist=pip_config[4],
			root=pip_config[5],
			saddleThd=pip_config[6],
			)
		f.write(to_write)
		f.close()
	else:
		print('[config]\tError creating file:', filename)


template_graph = """# vertex filename
{vertname}
# edge filename
{edgename}
# output prefix: program writes to output/0.swc
{outname}
# root
{root}
# threshold for simplification
{sadd_thd}
# component threshold C. Only component larger than C will be kept
{comp_thd}
"""

def getGraphConfig(file):
	cfg = getLines(file)
	if len(cfg) < 5:
		print('[getGraphConfig]: Parameter less than 5')
		return None
	# check file exist
	# check parameters
	return cfg

def writeGraphConfig(filename, graph_config):
	f = open(filename, 'w')
	if f is not None:
		to_write = template_graph.format(
			vertname=graph_config[0],
			edgename=graph_config[1],
			outname=graph_config[2],
			root=graph_config[3],
			sadd_thd=graph_config[4],
			comp_thd=graph_config[5]
			)
		f.write(to_write)
		f.close()
	else:
		print('[config]\tError creating file:', filename)

def getDefaultGraph():
	config = [
	'0_vert.txt',
	'0_edge.txt',
	'output/0',
	'0 0 0',
	'0'
	]
	return config

if __name__  == "__main__":
	config = getDefaultGraph()
	writeGraphConfig('output/test.ini', config)
	
