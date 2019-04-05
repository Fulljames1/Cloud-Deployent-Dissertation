def GenerateConfig(ctx):
  """Reads SSL certificate and key from a file."""
  ssl = {'name': '-'.join([ctx.env['deployment'],
                           ctx.env['name'],
                           'ssl']),
         'type': 'compute.v1.sslCertificate',
         'properties': {
             'certificate': '\n'.join([ctx.imports[ctx.properties['crt']],
                                       ctx.imports[ctx.properties['csr']]]),
             'privateKey': ctx.imports[ctx.properties['key']]}}
  return {'resources': [ssl]}