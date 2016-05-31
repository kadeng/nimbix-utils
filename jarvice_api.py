import requests
import json
import config_nimbix as config
import re

def jarvice(endpoint, **params):
	params['apikey'] = config.apikey
	params['username'] = config.username
	return requests.get('https://api.jarvice.com/jarvice/%s' % (endpoint), params=params).json()

def jarvice_post(endpoint, postdata):
	return requests.get('https://api.jarvice.com/jarvice/%s' % (endpoint), data=postdata).json()

def apps():
	return jarvice('apps')

def job_list():
	return jarvice('jobs')

def job_submit(template_name='launch_interactive', image='deep-learning-2', staging='true', machine='n0', **template_params):
	template_params['apikey'] = config.apikey
	template_params['username'] = config.username
	template_params['image'] = image
	template_params['staging'] = staging
	template_params['machine'] = machine

	with open('job_templates/%s.json' % (template_name), 'r') as fh:
		template_json = fh.read()
		def replacer(match):
			return template_params[match.group(1)]
		ttext = re.sub('#([a-zA-Z_]+)#', replacer, template_json)
	print ttext
	return jarvice_post('submit', ttext)

def job_info(job_number):
	return jarvice('info', number=job_number)

def job_connect_info(job_number):
	return jarvice('connect', number=job_number)

def job_terminate(job_number):
	return jarvice('terminate', number=job_number)

def job_shutdown(job_number):
	return jarvice('terminate', number=job_number)

def job_action(job_number, action):
	return jarvice('terminate', number=job_number, action=action)

def job_status(job_number):
	return jarvice('status', number=job_number)

def job_output(job_number):
	return jarvice('output', number=job_number, lines=lines)

def job_tail(job_number, lines=100):
	return jarvice('tail', number=job_number, lines=lines)

def list_available_machines():
	return jarvice('machines')

