export async function GET() {
  return Response.json({
    message: 'Hello from Vercel Bun API!',
    bun: process.versions.bun ?? null,
    node: process.versions.node ?? null,
  });
}

export async function POST(request: Request) {
  try {
    const body = await request.json();
    return Response.json({ received: body, timestamp: Date.now() });
  } catch (error) {
    return Response.json(
      { error: 'Invalid JSON body', details: error instanceof Error ? error.message : String(error) },
      { status: 400 }
    );
  }
}
