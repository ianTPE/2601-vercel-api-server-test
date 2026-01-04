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
    const now = new Date();
    const offset = 8 * 60 * 60 * 1000;
    const localDate = new Date(now.getTime() + offset);
    // Remove milliseconds and append timezone
    const timestamp = localDate.toISOString().replace(/\.\d{3}Z$/, '+08:00');
    return Response.json({ received: body, timestamp });
  } catch (error) {
    return Response.json(
      { error: 'Invalid JSON body', details: error instanceof Error ? error.message : String(error) },
      { status: 400 }
    );
  }
}
