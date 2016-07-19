import sys
from _app import run_app

def main( args = None ):
   if args is None:
      args = sys.argv[ 1 : ]

   result = run_app( args )

   return result

if __name__ == "__main__":
   sys.exit( main( sys.argv[ 1 : ] ) )
